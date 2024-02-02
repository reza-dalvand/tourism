from rest_framework.permissions import AllowAny, DjangoObjectPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.core.permissions.check_object_owner import CheckObjectOwner
from apps.hotels.models import Room
from apps.hotels.serializers import RoomSerializer


class RoomApi(ModelViewSet):
    permission_classes = (AllowAny, CheckObjectOwner)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
