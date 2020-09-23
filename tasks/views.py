from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from main.templatetags.main_tags import naturaltime
from .forms import CreateTaskUserForm, UpdateTaskForm
from .models import Task


class TasksListView(ListView):
    model = Task
    paginate_by = 10


class TaskCreateView(CreateView):
    model = Task
    form_class = CreateTaskUserForm
    success_url = reverse_lazy('task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_message_button'] = _('Create')
        context['reset_message_button'] = _('Reset')
        return context


class TaskDetailView(DetailView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_time'] = naturaltime(context['task'].create_time)
        return context


class TaskUpdateView(UpdateView):
    model = Task
    form_class = UpdateTaskForm
    success_url = reverse_lazy('task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_message_button'] = _('Apply')
        context['reset_message_button'] = _('Reset')
        return context

    def post(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, _('Task updated!'))
        return super().post(request, *args, **kwargs)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_message_button'] = _('Delete')
        return context

    def post(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, _('Task deleted!'))
        return super().post(request, *args, **kwargs)
