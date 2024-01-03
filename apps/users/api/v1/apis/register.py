from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.users.serializers import RegisterSerializer


# # Customize Register
class RegisterApi(generics.CreateAPIView):
    """
    handel registration with phone number and password

    Parameters:
        - email: String
        - password: String
    """

    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
