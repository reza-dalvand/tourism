from django.db import models
from django.db.models import Q


class RoomQuerySet(models.QuerySet):
    """return rooms which are not reserved"""

    def unreserved_rooms(self):
        return self.filter(Q(entry_date__isnull=True) and Q(exit_date__isnull=True))
