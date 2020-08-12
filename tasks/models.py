from colorfield.fields import ColorField
from django.db import models
from django.utils.translation import gettext_lazy as _

from persons.models import Person


class Task(models.Model):
	subject = models.CharField(verbose_name=_('Subject'), max_length=100)
	description = models.TextField(verbose_name=_('Comment'))
	tags = models.ManyToManyField('Tag', verbose_name=_('Tags'), blank=True)
	persons = models.ManyToManyField(Person, blank=True)
	status = models.ForeignKey('Status', verbose_name=_('Status'), on_delete=models.PROTECT)
	project = models.ForeignKey('Project', verbose_name=_('Project'), on_delete=models.PROTECT)

	class Meta:
		verbose_name = _('Task')
		verbose_name_plural = _('Tasks')

	def __str__(self):
		return self.subject


class Project(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=100)
	description = models.TextField(verbose_name=_('Description'))

	class Meta:
		verbose_name = _('Project')
		verbose_name_plural = _('Projects')

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=50)
	color = ColorField(verbose_name=_('Color'), default='#FFFFFF')

	class Meta:
		verbose_name = _('Tag')
		verbose_name_plural = _('Tags')

	def __str__(self):
		return self.name


class Status(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=50)
	is_closed = models.BooleanField(verbose_name=_('Closed?'), default=False)

	class Meta:
		verbose_name = _('Status')
		verbose_name_plural = _('Statuses')

	def __str__(self):
		return self.name
