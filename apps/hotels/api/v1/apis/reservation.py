from django.db import IntegrityError
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
        hotel = serializer.validated_data.get("hotel")
        entry_date = serializer.validated_data.get("entry_date")
        reserve = Reservation.objects.select_related("hotel", "room").filter(hotel=hotel, room=room).first()
        try:
            if not reserve or reserve.exit_date < entry_date:
                return super().create(request, *args, **kwargs)
            return Response(data=_("This room already reserved"), status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError as e:
            return Response(data=_("You can't reserve this room again"), status=status.HTTP_400_BAD_REQUEST)
