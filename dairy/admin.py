from django.contrib import admin

from .models import Article
from django.db import models

from markitup.widgets import AdminMarkItUpWidget


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    article_overrides = {models.TextField: {'widget': AdminMarkItUpWidget}}
    list_display = ('id', 'day')
    list_filter = ('day',)
