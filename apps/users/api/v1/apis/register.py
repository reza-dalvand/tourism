from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.services.send_otp import send_and_save_otp_code
from apps.utils.generate_otp import check_expire_otp


class RegisterApi(generics.CreateAPIView):
    """
    handel registration with mobile number

    Parameters:
        - mobile: String
    """

    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        user = kwargs.get("user")
        if not check_expire_otp(user):
            send_and_save_otp_code(user)
            return Response({"status": "Ok"}, status=status.HTTP_201_CREATED)
        return Response("The otp code has not expired", status=status.HTTP_400_BAD_REQUEST)
