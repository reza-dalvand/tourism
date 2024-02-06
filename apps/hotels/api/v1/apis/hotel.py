from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.core.permissions.check_hotel_owner import CheckHotelOwner
from apps.hotels.models import Hotel
from apps.hotels.serializers import HotelSerializer


class HotelApi(ModelViewSet):
    """
    create change or ... after checking user is allowed
    to access this operation (with CheckHotelOwner)

    """

    permission_classes = (IsAuthenticated, CheckHotelOwner)
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
