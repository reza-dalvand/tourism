from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

User = get_user_model()


class TourismCompony(BaseModel):
    compony_name = models.CharField(_("name"), max_length=150, primary_key=True)
    short_des = models.CharField(_("short description"), max_length=250)
    description = models.TextField(_("description"))

    class Meta:
        verbose_name = _("compony")
        verbose_name_plural = _("companies")

    def __str__(self):
        return self.name
