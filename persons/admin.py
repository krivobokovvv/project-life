# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Person, Contact, ContactType, Company


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'first_name',
		'middle_name',
		'last_name',
		'birthday',
		'company',
		'position',
		'deleted',
	)
	list_filter = ('birthday', 'company', 'deleted')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'person', 'contact_type')
	list_filter = ('person', 'contact_type')


@admin.register(ContactType)
class ContactTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'regex')
	search_fields = ('name',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	search_fields = ('name',)
