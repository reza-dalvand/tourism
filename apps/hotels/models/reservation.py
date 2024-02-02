from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Q, UniqueConstraint
from django.utils.translation import gettext_lazy as _

from apps.users.models import User

from .hotel import Hotel
from .room import Room


class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotels")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="rooms")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    entry_date = models.DateTimeField(null=True, blank=True)
    exit_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _("reserve")
        verbose_name_plural = _("reservation")
        constraints = [
            UniqueConstraint(fields=["hotel", "room", "user"], name="constraint_unique"),
            models.CheckConstraint(check=Q(entry_date__lt=F("exit_date")), name="check_reserve_date"),
        ]

    def __str__(self):
        return f"user {self.user} has reserved room {self.room} of {self.hotel}"
