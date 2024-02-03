from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.core.permissions.check_hotel_owner import CheckHotelOwner
from apps.hotels.models import Room
from apps.hotels.serializers import RoomSerializer


class RoomApi(ModelViewSet):
    permission_classes = (AllowAny, CheckHotelOwner)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
