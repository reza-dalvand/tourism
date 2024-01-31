from django.core.validators import MaxValueValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.regex_patterns import LANDING_PHONE_PATTERN


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    name = models.CharField(_("name"), max_length=150)
    phone = models.CharField(
        _("phone"),
        max_length=11,
        validators=[
            RegexValidator(regex=LANDING_PHONE_PATTERN, message=_("Enter a valid mobile number"), code="Invalid Number")
        ],
    )
    email = models.EmailField(_("email"), max_length=200)
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
        return self.name
