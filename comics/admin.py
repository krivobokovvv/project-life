# -*- coding: utf-8 -*-
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Book, Chapter, Page, Tag


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	raw_id_fields = ('tags',)
	search_fields = ('name',)


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
	list_display = ('id', 'book', 'name', 'count_page')
	list_filter = ('book',)
	search_fields = ('name',)


@admin.register(Page)
class PageAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('id', 'chapter', 'number', 'image')
	list_filter = ('chapter',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'color')
	search_fields = ('name',)
