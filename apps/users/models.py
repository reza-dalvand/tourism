from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
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
        validators=[
            RegexValidator(regex=PHONE_REGEX, message="Enter a valid phone number", code="Invalid Registration Number")
        ],
    )
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
