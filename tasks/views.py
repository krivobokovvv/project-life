from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import CreateTaskUserForm, UpdateTaskForm
from .models import Task


class TasksListView(ListView):
	model = Task
	template_name = "tasks/task_list.html"
	paginate_by = 10


class TaskCreateView(CreateView):
	model = Task
	template_name = "tasks/task_create.html"
	form_class = CreateTaskUserForm
	success_url = reverse_lazy('task-list')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['submit_message_button'] = _('Create')
		return context


class TaskDetailView(DetailView):
	model = Task
	template_name = "tasks/task_detail.html"


class TaskUpdateView(UpdateView):
	model = Task
	template_name = "tasks/task_update.html"
	form_class = UpdateTaskForm
	success_url = reverse_lazy('task-list')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['submit_message_button'] = _('Update')
		return context

	def post(self, request, *args, **kwargs):
		messages.add_message(request, messages.SUCCESS, _('Task updated!'))
		return super().post(request, *args, **kwargs)


class TaskDeleteView(DeleteView):
	model = Task
	template_name = "tasks/task_delete.html"
	success_url = reverse_lazy('task-list')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['submit_message_button'] = _('Delete')
		return context

	def post(self, request, *args, **kwargs):
		messages.add_message(request, messages.SUCCESS, _('Task deleted!'))
		return super().post(request, *args, **kwargs)
