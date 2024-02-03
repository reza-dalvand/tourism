from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.core.permissions.check_reserve_owner import CheckReserveOwner
from apps.hotels.models import Reservation
from apps.hotels.serializers import HotelReservationSerializer


class HotelReservation(ModelViewSet):
    permission_classes = (AllowAny, CheckReserveOwner)
    serializer_class = HotelReservationSerializer
    queryset = Reservation.objects.all()
