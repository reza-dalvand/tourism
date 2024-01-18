from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.services.send_otp import send_sms
from apps.users.models import User
from apps.users.serializers import RegisterSerializer, VerifyRegistrationSerializer
from apps.utils.generate_otp import check_expire_otp, generate_otp_code


class RegisterApi(generics.CreateAPIView):
    """
    handel registration with mobile number

    Parameters:
        - mobile: String
    """

    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # If the user has already been created but not activated
        user, created = User.objects.get_or_create(mobile=serializer.data.get("mobile"))
        if user.is_active:
            return Response("This account has already been activated", status=status.HTTP_400_BAD_REQUEST)
        elif created or not check_expire_otp(user):
            otp_code = generate_otp_code()
            user.otp = otp_code
            user.save()
            send_sms(user, otp_code)
            return Response({"status": "Ok"}, status=status.HTTP_201_CREATED)
        return Response("The otp code has not expired", status=status.HTTP_400_BAD_REQUEST)


class VerifyRegistrationApi(APIView):
    """
    handel verify registration with mobile number and otp code

    Parameters:
        - mobile: String
        - otp: String
    """

    permission_classes = (AllowAny,)

    def post(self, request, **kwargs):
        serializer = VerifyRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.data.get("mobile")
        code = serializer.data.get("code")
        user = get_object_or_404(User, mobile=mobile)
        if check_expire_otp(user) and user.otp == code:
            user.is_active = True
            user.otp = None
            user.save(update_fields=["otp", "is_active"])
            return Response(data={"status": "verified"}, status=status.HTTP_200_OK)
        return Response(data=_("Code is not correct"), status=status.HTTP_400_BAD_REQUEST)
