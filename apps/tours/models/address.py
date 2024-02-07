from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseAddressModel

from .company import TourismCompany


class TourismCompanyAddress(BaseAddressModel):
    company_name = models.ForeignKey(TourismCompany, on_delete=models.CASCADE, related_name="addresses")

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")

    def __str__(self):
        return f"{self.company_name} {self.city}"
