from colorfield.fields import ColorField
from django.db import models
from django.utils.translation import gettext_lazy as _

from persons.models import Person


class Task(models.Model):
	class Meta:
		verbose_name = _('Task')
		verbose_name_plural = _('Tasks')

	subject = models.CharField(verbose_name=_('Subject'), max_length=100)
	description = models.TextField(verbose_name=_('Comment'))
	tags = models.ManyToManyField('Tag', blank=True)
	persons = models.ManyToManyField(Person, blank=True)
	status = models.ForeignKey('Status', on_delete=models.PROTECT)
	project = models.ForeignKey('Project', on_delete=models.PROTECT)

	def __str__(self):
		return self.subject


class Project(models.Model):
	class Meta:
		verbose_name = _('Project')
		verbose_name_plural = _('Projects')

	name = models.CharField(verbose_name=_('Name'), max_length=100)
	description = models.TextField(verbose_name=_('Description'))

	def __str__(self):
		return self.name


class Tag(models.Model):
	class Meta:
		verbose_name = _('Tag')
		verbose_name_plural = _('Tags')

	name = models.CharField(verbose_name=_('Name'), max_length=50)
	color = ColorField(default='#FFFFFF')

	def __str__(self):
		return self.name


class Status(models.Model):
	class Meta:
		verbose_name = _('Status')
		verbose_name_plural = _('Statuses')

	name = models.CharField(verbose_name=_('Name'), max_length=50)
	is_closed = models.BooleanField(verbose_name=_('Closed?'), default=False)

	def __str__(self):
		return self.name
