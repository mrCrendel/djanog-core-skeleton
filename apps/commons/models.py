from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimestampAbstractModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(verbose_name=_('Создано'), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name=_('Обновлено'), auto_now=True, null=True)

    def __str__(self):
        pass
