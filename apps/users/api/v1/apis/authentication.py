from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.services.send_otp import send_otp_code
from apps.users.models import User
from apps.users.serializers import LoginOrRegisterSerializer
from apps.utils.generate_otp import check_expire_otp


class LoginOrRegisterApi(APIView):
    permission_classes = (AllowAny,)
    throttle_scope = "auth"

    def post(self, request, *args, **kwargs):
        serializer = LoginOrRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data.get("mobile")
        user, created = User.objects.using("users").get(mobile=mobile)
        if created or check_expire_otp(user):
            send_otp_code(user)
        else:
            return Response(data="The otp code is not expired", status=status.HTTP_400_BAD_REQUEST)

        if user.is_active:
            return Response(data={"status": "Login success"}, status=status.HTTP_200_OK)
        return Response(data={"status": "User was registered"}, status=status.HTTP_201_CREATED)
