from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User
from apps.users.serializers import RegisterSerializer, VerifyRegistrationSerializer


class RegisterApi(generics.CreateAPIView):
    """
    handel registration with phone number

    Parameters:
        - phone: String
    """

    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class VerifyRegistrationApi(APIView):
    """
    handel verify registration with phone number and otp code

    Parameters:
        - phone: String
        - otp: String
    """

    permission_classes = (AllowAny,)

    def post(self, request, **kwargs):
        serializer = VerifyRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.data.get("phone")
        code = serializer.data.get("code")
        user = get_object_or_404(User, phone=phone)
        print("test data", request.data, user.otp, code)

        if user.otp == code and len(code) == 6:
            user.is_active = True
            user.otp = None
            user.save()
            return Response(data=f"{user.phone} is verified", status=status.HTTP_200_OK)
        return Response(data=_("code is wrong"), status=status.HTTP_409_CONFLICT)
