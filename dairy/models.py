from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from markitup.fields import MarkupField

from generic.models import DateTimeMixin


class Article(DateTimeMixin):
    day = models.DateField(unique=True)
    text = MarkupField()
    rating = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def get_format_name(self):
        pass

    def __str__(self):
        return f'{self.day}'
