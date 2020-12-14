from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DairyConfig(AppConfig):
    name = 'dairy'
    verbose_name = _('Dairy')
