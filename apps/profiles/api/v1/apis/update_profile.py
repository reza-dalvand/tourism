from django.contrib.auth import get_user_model
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.profiles.serializers import UpdateProfileSerializer

User = get_user_model()


class UpdateProfile(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateProfileSerializer
    queryset = User.objects.all()
