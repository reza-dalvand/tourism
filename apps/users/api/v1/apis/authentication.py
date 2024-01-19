from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from apps.users.models import User
from apps.users.serializers import LoginOrRegisterSerializer

from .auth_apis.login import LoginApi
from .auth_apis.register import RegisterApi


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
