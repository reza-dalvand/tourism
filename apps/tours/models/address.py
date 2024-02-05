from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseAddress

from .compony import TourismCompony


class TourismComponyAddress(BaseAddress):
    compony_name = models.ForeignKey(TourismCompony, on_delete=models.CASCADE, related_name="addresses")

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")

    def __str__(self):
        return f"{self.compony_name} {self.city}"
