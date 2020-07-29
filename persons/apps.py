from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PersonsConfig(AppConfig):
    name = 'persons'
    verbose_name = _('Persons')