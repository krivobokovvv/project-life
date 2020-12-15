from django.urls import path

from .views import DairyListView, DairyDetailView, DairyCreateView, DairyUpdateView

urlpatterns = (
    path('', DairyListView.as_view(), name='dairy-list'),
    path('task/create/', DairyCreateView.as_view(), name='dairy-create'),
    path('dairy/<int:pk>/detail', DairyDetailView.as_view(), name='dairy-detail'),
    path('task/<int:pk>/update', DairyUpdateView.as_view(), name='dairy-update'),
    #path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
)
