from django.contrib import admin

from .models import Dairy
from django.db import models

from markitup.widgets import AdminMarkItUpWidget


@admin.register(Dairy)
class DairyAdmin(admin.ModelAdmin):
    article_overrides = {models.TextField: {'widget': AdminMarkItUpWidget}}
    list_display = ('id', 'day', 'format', 'article')
    list_filter = ('day',)
