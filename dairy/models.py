from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class FORMAT(models.IntegerChoices):
    md = 1, 'Markdown'
    bbcode = 2, 'BBCode'
    rst = 3, 'reStructuredText'


class Dairy(models.Model):
    day = models.DateField(unique=True)
    text = models.TextField
    format = models.PositiveSmallIntegerField(
        choices=FORMAT.choices,
        default=FORMAT.bbcode
    )
    article = models.TextField()

    def __str__(self):
        return f'{self.day}'
