from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.core.permissions.check_hotel_owner import CheckHotelOwner
from apps.hotels.models import Hotel
from apps.hotels.serializers import HotelSerializer


class HotelApi(ModelViewSet):
    """
    CRUD operation after verifying the user is authorized
    To access it with CheckTourCompanyOwner permission

    """

    permission_classes = (IsAuthenticated, CheckHotelOwner)
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
