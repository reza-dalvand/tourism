from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.hotels.models import Hotel


class HotelAddress(models.Model):
    CITIES = {
        "Tehran": _("Tehran"),
        "Kish": _("Kish"),
        "Mashhad": _("Mashhad"),
        "Yazd": _("Yazd"),
    }
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="addresses")
    city = models.CharField(_("city"), max_length=255, choices=CITIES)
    lang = models.DecimalField(_("lang"), max_digits=17, decimal_places=10)
    lat = models.DecimalField(_("lang"), max_digits=17, decimal_places=10)
    address = models.TextField(_("address"))

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")

    def __str__(self):
        return f"{self.hotel} {self.city}"
