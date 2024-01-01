from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.users.serializers import RegisterSerializer


class RegisterApi(generics.CreateAPIView):
    """
    handel registration with phone number and password

    Parameters:
        - phone: String
        - email: String
        - password: String

    Returns:
        - phone: String
        - email: String
    """

    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
