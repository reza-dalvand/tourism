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
        validators=[RegexValidator(regex=MOBILE_PATTERN, message="Enter a valid mobile number", code="Invalid Number")],
    )
    email = models.EmailField(_("email address"), null=True, blank=True)
    email_is_verified = models.BooleanField(_("is verified"), default=False)
    is_active = models.BooleanField(_("is active"), default=False)
    avatar = models.FileField(
        _("avatar"),
        upload_to="avatars/%y/%m/%d",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png"])],
    )
    otp = models.PositiveSmallIntegerField(verbose_name=_("otp code"), blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)

    address = models.TextField(null=True, blank=True)

    USERNAME_FIELD = "mobile"

    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.mobile
