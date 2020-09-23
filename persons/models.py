from django.db import models
from django.utils.translation import gettext_lazy as _

from generic.models import Model


class Person(Model):
	first_name = models.CharField(verbose_name=_('First name'), max_length=100)
	middle_name = models.CharField(verbose_name=_('Middle name'), max_length=100, blank=True)
	last_name = models.CharField(verbose_name=_('Last name'), max_length=100, blank=True)
	birthday = models.DateField(verbose_name=_('Birthday'), blank=True, null=True)
	company = models.ForeignKey('Company', on_delete=models.PROTECT, blank=True, null=True)
	position = models.CharField(verbose_name=_('Position'), max_length=100, blank=True)
	nickname = models.CharField(verbose_name=_('Nickname'), max_length=30, blank=True)

	is_deleted = models.BooleanField(verbose_name=_('Deleted?'), default=False)

	class Meta:
		verbose_name = _('Person')
		verbose_name_plural = _('Persons')

	def __str__(self):
		if self.nickname:
			return self.nickname
		else:
			return f'{self.last_name} {self.first_name} {self.middle_name}'


class Contact(Model):
	person = models.ForeignKey('Person', on_delete=models.PROTECT)
	contact_type = models.ForeignKey('ContactType', on_delete=models.PROTECT)
	value = models.CharField(verbose_name=_('Value'), max_length=100)

	class Meta:
		verbose_name = _('Contact')
		verbose_name_plural = _('Contacts')

	def __str__(self):
		return f'{self.contact_type}: {self.value}'


class ContactType(Model):
	name = models.CharField(verbose_name=_('Name'), max_length=100)
	regex = models.CharField(verbose_name=_('Regular expression'), max_length=100)

	class Meta:
		verbose_name = _('Contact type')
		verbose_name_plural = _('Contact types')

	def __str__(self):
		return self.name


class Company(Model):
	name = models.CharField(verbose_name=_('Name'), max_length=100)
	address = models.CharField(verbose_name=_('Address'), max_length=150, blank=True)

	class Meta:
		verbose_name = _('Company')
		verbose_name_plural = _('Companies')

	def __str__(self):
		return self.name
