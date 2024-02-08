from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Q
from django.utils.translation import gettext_lazy as _

from apps.tours.managers import TourQuerySet

from .company import TourismCompany


class Tour(models.Model):
    company_name = models.ForeignKey(TourismCompany, related_name="tours", on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name="tours", on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=255)
    start_date = models.DateTimeField(_("Start Date"))
    end_date = models.DateTimeField(_("Start Date"))
    short_des = models.CharField(_("short description"), max_length=250)
    description = models.TextField(_("description"))
    price = models.DecimalField(_("price"), max_digits=8, decimal_places=2)
    capacity = models.PositiveSmallIntegerField(_("capacity"))

    objects = TourQuerySet.as_manager()

    class Meta:
        verbose_name = _("tour")
        verbose_name_plural = _("tours")
        constraints = [
            models.CheckConstraint(
                check=Q(start_date__lt=F("end_date")),
                name="check_tour_date",
                violation_error_message=_("thr end date cannot be set less than or equal to the start date"),
            ),
        ]

    def __str__(self):
        return f"{self.company_name} {self.title}"
