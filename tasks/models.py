from colorfield.fields import ColorField
from django.db import models
from django.utils.translation import gettext_lazy as _

from generic.models import Model, DateTimeMixin
from persons.models import Person


class Task(DateTimeMixin):
    subject = models.CharField(verbose_name=_('Subject'), max_length=100)
    description = models.TextField(verbose_name=_('Comment'), blank=True)
    tags = models.ManyToManyField('Tag', verbose_name=_('Tags'), blank=True)
    persons = models.ManyToManyField(Person, blank=True)
    status = models.ForeignKey('Status', verbose_name=_('Status'), on_delete=models.PROTECT)
    project = models.ForeignKey('Project', verbose_name=_('Project'), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return self.subject


class Project(DateTimeMixin):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    parent = models.ForeignKey('self', verbose_name=_('Parent project'), blank=True, null=True,
                               on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.name


class Tag(Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    color = ColorField(verbose_name=_('Color'), default='#FFFFFF')

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.name


class Status(Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    is_closed = models.BooleanField(verbose_name=_('Closed?'), default=False)

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')

    def __str__(self):
        return self.name
