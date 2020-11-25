from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from main.templatetags.main_tags import naturaltime
from .forms import TaskForm
from .models import Task


class TasksListView(ListView):
    paginate_by = 10
    queryset = Task.objects.filter(status__is_closed=False).order_by('-change_time')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Create task')
        return context


class TaskDetailView(DetailView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Update task')
        return context

    def post(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, _('Task updated!'))
        return super().post(request, *args, **kwargs)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, _('Task deleted!'))
        return super().post(request, *args, **kwargs)
