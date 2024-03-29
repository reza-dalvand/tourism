from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.tours.models.company import TourismCompany
from apps.tours.models.tour import Tour


class TourReservation(models.Model):
    company_name = models.ForeignKey(TourismCompany, related_name="tour_reservations", on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name="tour_reservations", on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, related_name="tour_reservations", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("reservation")
        verbose_name_plural = _("reservations")
        constraints = [
            UniqueConstraint(fields=["company_name", "user", "tour"], name="constraint_tour_unique"),
        ]

    def __str__(self):
        return f"{self.company_name} {self.tour.title}"


@receiver(pre_save, sender=TourReservation)
def check_capacity(sender, instance, **kwargs):
    """check Tour Capacity before save reservation"""
    reservation_count = TourReservation.objects.count()
    if instance.tour.capacity < reservation_count:
        raise ValidationError("Tour Capacity is fulled")
