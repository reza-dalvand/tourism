from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel, PhoneAndEmailModel


class TourismCompany(BaseModel, PhoneAndEmailModel):
    company_name = models.CharField(_("name"), max_length=150, primary_key=True)
    short_des = models.CharField(_("short description"), max_length=250)
    description = models.TextField(_("description"))

    class Meta:
        verbose_name = _("company")
        verbose_name_plural = _("companies")

    def __str__(self):
        return self.company_name
