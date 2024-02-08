from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.core.permissions.check_reserve_owner import CheckReserveOwner
from apps.tours.models import TourReservation
from apps.tours.serializers import TourReservationSerializer


class TourReservationApi(ModelViewSet):
    """
    CRUD operation after verifying the user is authorized
    To access it with CheckReserveOwner permission

    """

    permission_classes = (IsAuthenticated, CheckReserveOwner)
    serializer_class = TourReservationSerializer
    queryset = TourReservation.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            self.create(request, *args, **kwargs)
        except ValidationError:
            return Response(data=_("Tour Capacity is fulled"), status=status.HTTP_403_FORBIDDEN)
