from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.core.permissions.check_owner import CheckOwner
from apps.hotels.models import Room
from apps.hotels.serializers import RoomSerializer


class RoomApi(ModelViewSet):
    permission_classes = (AllowAny, CheckOwner)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
