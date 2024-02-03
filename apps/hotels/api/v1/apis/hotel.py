from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.core.permissions.check_hotel_owner import CheckHotelOwner
from apps.hotels.models import Hotel
from apps.hotels.serializers import HotelSerializer


class HotelApi(ModelViewSet):
    permission_classes = (AllowAny, CheckHotelOwner)
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
