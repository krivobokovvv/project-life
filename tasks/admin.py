# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Task, Project, Tag, Status


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ('id', 'subject', 'description', 'status')
	list_filter = ('status',)
	raw_id_fields = ('tags', 'persons')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description')
	search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'color')
	search_fields = ('name',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'closed')
	list_filter = ('closed',)
	search_fields = ('name',)
