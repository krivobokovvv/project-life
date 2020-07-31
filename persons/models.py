from django.db import models
from django.utils.translation import gettext_lazy as _

class Person(models.Model):
	class Meta:
		verbose_name = _('Person')
		verbose_name_plural = _('Persons')

	first_name = models.CharField(verbose_name=_('First name'), max_length=100)
	middle_name = models.CharField(verbose_name=_('Middle name'), max_length=100, blank=True, null=True)
	last_name = models.CharField(verbose_name=_('Last name'), max_length=100, blank=True, null=True)
	birthday = models.DateField(verbose_name=_('Birthday'), blank=True, null=True)
	company = models.ForeignKey('Company', on_delete=models.PROTECT, blank=True, null=True)
	position = models.CharField(verbose_name=_('Position'), max_length=100, blank=True, null=True)
	nick = models.CharField(verbose_name=_('Nick'), max_length=30, blank=True, null=True)

	deleted = models.BooleanField(verbose_name=_('Deleted?'), default=False)

	def __str__(self):
		if self.nick is not None:
			return self.nick
		else:
			return f'{self.last_name} {self.first_name} {self.middle_name}'


class Contact(models.Model):
	class Meta:
		verbose_name = _('Contact')
		verbose_name_plural = _('Contacts')

	person = models.ForeignKey('Person', on_delete=models.PROTECT)
	contact_type = models.ForeignKey('ContactType',on_delete=models.PROTECT)
	value = models.CharField(verbose_name=_('Value'), max_length=100)

	def __str__(self):
		return f'{self.contact_type}: {self.value}'


class ContactType(models.Model):
	class Meta:
		verbose_name = _('Contact type')
		verbose_name_plural = _('Contact types')
	
	name = models.CharField(verbose_name=_('Name'), max_length=100)
	regex = models.CharField(verbose_name=_('Regular expression'), max_length=100, blank=True, null=True)

	def __str__(self):
		return self.name


class Company(models.Model):
	class Meta:
		verbose_name = _('Company')
		verbose_name = _('Companies')

	name = models.CharField(verbose_name=_('Name'), max_length=100)
	address = models.CharField(verbose_name=_('Address'), max_length=150, blank=True, null=True)

	def __str__(self):
		return self.name