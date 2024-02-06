from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from .company import TourismCompany


class Tour(models.Model):
    company_name = models.ForeignKey(TourismCompany, related_name="tours", on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name="tours", on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=255)
    start_date = models.DateTimeField(_("Start Date"), blank=True, null=True)
    end_date = models.DateTimeField(_("Start Date"), blank=True, null=True)
    short_des = models.CharField(_("short description"), max_length=250)
    description = models.TextField(_("description"))
    price = models.DecimalField(_("price"), max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _("tour")
        verbose_name_plural = _("tours")

    def __str__(self):
        return f"{self.company_name} {self.title}"
