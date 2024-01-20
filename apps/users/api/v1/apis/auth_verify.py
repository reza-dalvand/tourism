from django.contrib.auth import login
from django.shortcuts import get_object_or_404
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
        - mobile: String
        - code: Integer
    """

    permission_classes = (AllowAny,)

    def post(self, request, **kwargs):
        serializer = VerifyOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.data.get("mobile")
        code = serializer.data.get("code")
        user = get_object_or_404(User, mobile=mobile)
        if check_expire_otp(user) and user.otp == code:
            user.is_active = True
            user.otp = None
            # Preventing otp_create_time field from being updated
            user.save(update_fields=["otp", "is_active"])
            login(request, user)
            refresh = RefreshToken.for_user(user)
            tokens = {
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token),
            }
            return Response(data=tokens, status=status.HTTP_200_OK)
        return Response(data=_("Code is not correct"), status=status.HTTP_400_BAD_REQUEST)
