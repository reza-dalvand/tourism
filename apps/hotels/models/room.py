from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from apps.hotels.models import Hotel


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    entry_date = models.DateField(_("entry date"), blank=True, null=True)
    exit_date = models.DateField(_("exit date"), blank=True, null=True)
    number_of_bed = models.IntegerField(_("number of bed"), default=2)
    has_wifi = models.BooleanField(_("has wifi"), default=True)
    has_bathroom = models.BooleanField(_("has bathroom "), default=True)

    class Meta:
        verbose_name = _("room")
        verbose_name_plural = _("rooms")
        constraints = [
            models.CheckConstraint(check=Q(entry_date__lt=models.F("exit_date")), name="check_reserve_date"),
        ]

    def __str__(self):
        return f"{self.hotel} {self.room_id}"
