from django.urls import path

from .views import TasksListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

app_name = 'tasks'

urlpatterns = (
    path('task/', TasksListView.as_view(), name='task-list'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/detail', TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
)
