from django.contrib.auth import login
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User
from apps.users.serializers import VerifyOtpSerializer
from apps.utils.generate_otp import check_expire_otp


class VerifyOtpApi(APIView):
    """
    handel verify registration with mobile number and otp code

    Parameters:
        - code: Integer

    Returns:
        dict: {refresh_token: string, access_token: string}
    """

    permission_classes = (AllowAny,)

    def post(self, request, **kwargs):
        serializer = VerifyOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = request.session.get("mobile")
        code = serializer.data.get("code")
        user = User.objects.using("users_db").get(mobile=mobile)
        if not check_expire_otp(user) and user.otp == code:
            user.is_active = True
            user.otp = None
            user.save(update_fields=["is_active", "otp"])
            login(request, user)
            refresh = RefreshToken.for_user(user)
            tokens = {
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token),
            }
            return Response(data=tokens, status=status.HTTP_200_OK)
        return Response(data=_("Code is invalid"), status=status.HTTP_400_BAD_REQUEST)
