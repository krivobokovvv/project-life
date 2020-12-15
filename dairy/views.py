from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import DairyForm
from .models import Dairy


class DairyListView(ListView):
    paginate_by = 10
    queryset = Dairy.objects.order_by('-day')


class DairyCreateView(CreateView):
    model = Dairy
    form_class = DairyForm
    success_url = reverse_lazy('dairy-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Create task')
        return context


class DairyDetailView(DetailView):
    model = Dairy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DairyUpdateView(UpdateView):
    model = Dairy
    form_class = DairyForm
    success_url = reverse_lazy('dairy-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Update task')
        return context

    def post(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, _('Task updated!'))
        return super().post(request, *args, **kwargs)