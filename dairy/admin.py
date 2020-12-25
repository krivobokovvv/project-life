from django.contrib import admin

from .models import Article
from django.db import models

from markitup.widgets import AdminMarkItUpWidget


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    text_overrides = {models.TextField: {'widget': AdminMarkItUpWidget}}
    list_display = (
        'id',
        'create_time',
        'change_time',
        'day',
        'text',
        'rating',
    )
    list_filter = ('create_time', 'change_time', 'day')
