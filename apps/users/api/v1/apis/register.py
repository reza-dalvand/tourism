from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.users.serializers import RegisterSerializer


class RegisterApi(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
