from django.db import models
from django.utils.translation import gettext_lazy as _

from markitup.fields import MarkupField

from generic.models import DateTimeMixin


class Article(DateTimeMixin):
    day = models.DateField(unique=True)
    text = models.TextField
    text = MarkupField()

    def get_format_name(self):
        pass

    def __str__(self):
        return f'{self.day}'
