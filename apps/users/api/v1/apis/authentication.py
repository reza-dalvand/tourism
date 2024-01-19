from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.services.send_otp import send_and_save_otp_code
from apps.users.models import User
from apps.users.serializers import LoginOrRegisterSerializer, VerifyOtpSerializer
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
                "refresh": str(refresh),
                "access_token": str(refresh.access_token),
            }
            return Response(data=tokens, status=status.HTTP_200_OK)
        return Response(data=_("Code is not correct"), status=status.HTTP_400_BAD_REQUEST)


class LoginOrRegisterApi(APIView):
    permission_classes = (AllowAny,)
    throttle_scope = "authentication"

    def post(self, request, *args, **kwargs):
        serializer = LoginOrRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data.get("mobile")
        user, created = User.objects.get_or_create(mobile=mobile)
        if user.is_active:
            return LoginApi.as_view()(request._request, user=user)
        return RegisterApi.as_view()(request._request, user=user)
