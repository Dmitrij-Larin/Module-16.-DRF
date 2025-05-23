from django.db import models
from users.models import NULLABLE
from django.utils.translation import gettext_lazy as _



class Section(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('Discription'), **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        ordering = ['id']


class Content(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_('Section'))
    title = models.CharField(max_length=150, verbose_name=_('Title'))
    content = models.TextField(verbose_name=_('Content'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Section Content')
        verbose_name_plural = _('Section Contents')
        ordering = ['id']
