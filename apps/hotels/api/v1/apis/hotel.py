from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import IsAuthenticated
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
        hotel_name = kwargs["pk"]
        hotel = Hotel.objects.get(hotel_name=hotel_name)
        # comments = Comment.objects.filter(content_type_id=7, object_id=1)
        content_type = ContentType.objects.get_for_model(hotel)
        comments = Comment.objects.filter(content_type=content_type, object_id=1)
        print(comments)
