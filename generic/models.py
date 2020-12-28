from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Model(models.Model):
    id = models.AutoField

    class Meta:
        abstract = True

    def get_admin_url(self):
        return reverse(f"admin:{self._meta.app_label}_{self._meta.model_name}_change", args=(self.id,))


class DateTimeMixin(Model):
    create_time = models.DateTimeField(verbose_name=_('Created time'), auto_now_add=True)
    change_time = models.DateTimeField(verbose_name=_('Change time'), auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-change_time',)

    def set_forced_change_time(self, time):
        change_time_field = self._meta.get_field('change_time')
        change_time_field.auto_now = False
        self.change_time = time
        self.save()
        change_time_field.auto_now = True
