from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.core.permissions.check_reserve_owner import CheckReserveOwner
from apps.tours.models import Tour
from apps.tours.serializers import TourSerializer


class TourApi(ModelViewSet):
    """
    CRUD operation after verifying the user is authorized
    To access it with CheckTourCompanyOwner permission

    """

    permission_classes = (IsAuthenticated, CheckReserveOwner)
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
