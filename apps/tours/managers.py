from django.db import models
from django.db.models import F, Q
from django.db.models.functions import Now


class TourQuerySet(models.QuerySet):
    """return tours which are activate"""

    def active_tours(self):
        return self.filter(start_date__gte=Now())
