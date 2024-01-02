from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.constants import VALID_PHONE_NUMBER
from apps.common.regex_patterns import PHONE_REGEX

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    phone = models.CharField(
        _("phone number"),
        max_length=11,
        unique=True,
        validators=[RegexValidator(regex=PHONE_REGEX, message=VALID_PHONE_NUMBER, code="Invalid Registration Number")],
    )
    email = models.EmailField(_("email address"), unique=True)
    is_verified = models.BooleanField(_("is verified"), default=False)
    avatar = models.FileField(
        _("avatar"),
        upload_to="avatars/%y/%m/%d",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png"])],
    )
    otp = models.PositiveSmallIntegerField(verbose_name=_("otp code"), blank=True, null=True)

    address = models.TextField(null=True, blank=True)

    USERNAME_FIELD = "phone"

    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email
