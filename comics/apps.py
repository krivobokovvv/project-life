from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ComicsConfig(AppConfig):
	name = 'comics'
	verbose_name = _('Comics')
