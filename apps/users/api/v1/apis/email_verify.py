from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from apps.users.models import User
from apps.users.serializers import CheckEmailSerializer


class CheckEmailApi(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = CheckEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        # if user:= User.objects.get_object_or_404(email=email):


class VerifyEmail(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        pass
