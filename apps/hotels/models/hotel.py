from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

User = get_user_model()


class Hotel(BaseModel):
    hotel_name = models.CharField(_("name"), max_length=150, primary_key=True)
    number_of_rooms = models.IntegerField(_("number of rooms"))
    short_des = models.CharField(_("short description"), max_length=250)
    description = models.TextField(_("description"))
    hotel_type = models.PositiveSmallIntegerField(
        _("hotel's star"),
        default=2,
        validators=[MaxValueValidator(limit_value=6, message=_("The type of hotel should not be more than 6"))],
    )

    class Meta:
        verbose_name = _("hotel")
        verbose_name_plural = _("hotels")

    def __str__(self):
        return self.hotel_name
