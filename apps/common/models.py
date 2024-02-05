from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.regex_patterns import LANDING_PHONE_PATTERN
from apps.utils.fields.current_user import CurrentUserField


class BaseModel(models.Model):
    """A base model for every model."""

    owner = CurrentUserField(
        related_name="%(class)s_owner",
        on_delete=models.SET_NULL,
    )
    modifier = CurrentUserField(
        on_update=True,
        related_name="%(class)s_modifier",
        on_delete=models.SET_NULL,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    phone = models.CharField(
        _("phone"),
        max_length=11,
        validators=[
            RegexValidator(regex=LANDING_PHONE_PATTERN, message=_("Enter a valid mobile number"), code="Invalid Number")
        ],
    )
    email = models.EmailField(_("email"), max_length=200)

    class Meta:
        ordering = ["-id"]
        abstract = True


class BaseAddress(models.Model):
    CITIES = {
        "tehran": _("Tehran"),
        "kish": _("Kish"),
        "mashhad": _("Mashhad"),
        "yazd": _("Yazd"),
    }
    city = models.CharField(_("city"), max_length=255, choices=CITIES)
    lang = models.DecimalField(_("lang"), max_digits=17, decimal_places=10)
    lat = models.DecimalField(_("lang"), max_digits=17, decimal_places=10)
    address = models.TextField(_("address"))

    class Meta:
        abstract = True
