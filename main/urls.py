from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from .views import *

urlpatterns = (
	path('', IndexView.as_view(), name='index'),
)
