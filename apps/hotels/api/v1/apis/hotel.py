from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.comments.models import Comment
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

    def retrieve(self, request, *args, **kwargs):
        """added hotel's comments to response"""
        hotel = self.get_object()
        serializer = self.get_serializer(hotel)
        content_type = ContentType.objects.get_for_model(hotel)
        comments = Comment.objects.filter(content_type=content_type).values()
        # serializer.data is read only property
        serializer_data = serializer.data
        serializer_data["comments"] = list(comments)
        return Response(serializer_data, status=status.HTTP_200_OK)
