from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.regex_patterns import PHONE_REGEX

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    phone = models.CharField(
        _("phone number"),
        max_length=11,
        unique=True,
        null=True,
        blank=True,
        validators=[
            RegexValidator(regex=PHONE_REGEX, message="Enter a valid phone number", code="Invalid Registration Number")
        ],
    )
    email = models.EmailField(_("email address"), unique=True)
    email_is_verified = models.BooleanField(_("is verified"), default=False)
    phone_is_verified = models.BooleanField(_("is verified"), default=False)
    avatar = models.FileField(
        _("avatar"),
        upload_to="avatars/%y/%m/%d",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png"])],
    )
    otp = models.PositiveSmallIntegerField(verbose_name=_("otp code"), blank=True, null=True)

    address = models.TextField(null=True, blank=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["phone"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email
