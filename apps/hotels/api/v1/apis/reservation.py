from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.core.permissions.check_reserve_owner import CheckReserveOwner
from apps.hotels.models import Reservation
from apps.hotels.serializers import HotelReservationSerializer


class HotelReservation(ModelViewSet):
    """
    CRUD operation after verifying the user is authorized
    To access it with CheckReserveOwner permission

    """

    permission_classes = (IsAuthenticated, CheckReserveOwner)
    serializer_class = HotelReservationSerializer
    queryset = Reservation.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        room = serializer.validated_data.get("room")
        user = serializer.validated_data.get("user")
        hotel = serializer.validated_data.get("hotel")

        is_reserved = (
            Reservation.objects.select_related("hotel", "user", "room")
            .filter(hotel=hotel, room=room, user=user, entry_date__isnull=False, exit_date__isnull=False)
            .exists()
        )

        if not is_reserved:
            return super().create(request, *args, **kwargs)
        return Response(data=_("This room already reserved"), status=status.HTTP_403_FORBIDDEN)
