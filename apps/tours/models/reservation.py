from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.tours.models.company import TourismCompany
from apps.tours.models.tour import Tour


class TourReservation(models.Model):
    company_name = models.ForeignKey(TourismCompany, related_name="tour_reservations", on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name="tour_reservations", on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, related_name="tour_reservations", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("ture")
        verbose_name_plural = _("tours")

    def __str__(self):
        return f"{self.company_name} {self.tour.title}"
