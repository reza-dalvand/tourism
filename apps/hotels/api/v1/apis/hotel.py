from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.core.permissions.check_object_owner import CheckObjectOwner
from apps.hotels.models import Hotel
from apps.hotels.serializers import HotelSerializer


class HotelApi(ModelViewSet):
    permission_classes = (AllowAny, CheckObjectOwner)
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
