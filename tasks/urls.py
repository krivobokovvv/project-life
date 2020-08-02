from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from .views import *

urlpatterns = (
	path('task/', TasksListView.as_view(), name='task-list'),
	path('task/create/', TaskCreateView.as_view(), name='task-create'),
	path('task/detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
	path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
	path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
)
