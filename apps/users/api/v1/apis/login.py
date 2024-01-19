from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.services.send_otp import send_and_save_otp_code
from apps.utils.generate_otp import check_expire_otp


class LoginApi(APIView):
    """
    handel login user with mobile number

    Parameters:
        - mobile: string
    """

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user = kwargs.get("user")
        if not check_expire_otp(user):
            send_and_save_otp_code(user)
            return Response(data={"status": "Ok"}, status=status.HTTP_200_OK)
        return Response(data="The otp code has not expired", status=status.HTTP_400_BAD_REQUEST)
