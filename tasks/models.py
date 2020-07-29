from django.db import models
from django.utils.translation import ugettext_lazy as _

from persons.models import Person

from colorfield.fields import ColorField


class Task(models.Model):
	class Meta:
		verbose_name = _('Task')
		verbose_name_plural = _('Tasks')

	subject = models.CharField(verbose_name=_('Subject'), max_length=100)
	description = models.TextField(verbose_name=_('Comment'), blank=True, null=True)
	tags = models.ManyToManyField('Tag', blank=True)
	persons = models.ManyToManyField(Person, blank=True)
	status = models.ForeignKey('Status', on_delete=models.PROTECT)

	def __str__(self):
		return self.subject


class Project(models.Model):
	class Meta:
		verbose_name = _('Project')
		verbose_name_plural = _('Projects')

	name = models.CharField(verbose_name=_('Name'), max_length=100)
	description = models.TextField(verbose_name=_('Description'), blank=True, null=True)


class Tag(models.Model):
	class Meta:
		verbose_name = _('Tag')
		verbose_name_plural = _('Tags')

	name = models.CharField(verbose_name=_('Name'), max_length=50)
	color = ColorField(default='#FFFFFF')


class Status(models.Model):
	class Meta:
		verbose_name = _('Status')
		verbose_name_plural = _('Statuses')
	
	name = models.CharField(verbose_name=_('Name'), max_length=50)
	closed = models.BooleanField(verbose_name=_('Closed?'), default=False)
