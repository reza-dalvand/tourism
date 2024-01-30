import uuid as uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.regex_patterns import MOBILE_PATTERN

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    mobile = models.CharField(
        _("mobile"),
        max_length=11,
        unique=True,
        null=True,
        blank=True,
        validators=[
            RegexValidator(regex=MOBILE_PATTERN, message=_("Enter a valid mobile number"), code="Invalid Number")
        ],
    )
    email = models.EmailField(_("email address"), blank=True, null=True)
    email_is_verified = models.BooleanField(_("is verified"), default=False)
    is_active = models.BooleanField(_("is active"), default=False)
    avatar = models.FileField(
        _("avatar"),
        upload_to="avatars/%y/%m/%d",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png"])],
    )
    age = models.PositiveSmallIntegerField(_("age"), blank=True, null=True)
    otp = models.PositiveSmallIntegerField(_("otp code"), blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(_("uuid"), default=uuid.uuid4, editable=False)

    address = models.TextField(_("address"), null=True, blank=True)

    USERNAME_FIELD = "mobile"

    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()
    backend = "apps.users.backend.MobileBackend"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.mobile
