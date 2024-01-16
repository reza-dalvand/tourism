import logging

from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.services.send_otp import send_sms
from apps.users.serializers import RegisterSerializer
from apps.utils.generate_otp import generate_otp_code

logger = logging.getLogger("main")


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

    def perform_create(self, serializer):
        user = serializer.save(commit=False)
        otp = generate_otp_code()
        try:
            user.otp = otp
            send_sms(user, otp)
            print(otp)
        except Exception as e:
            logger.exception(e)

        return user
