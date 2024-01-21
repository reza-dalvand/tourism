from django.apps import apps
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User
from apps.utils.send_email import send_email


# Create your views here.
class TestView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        model_class = apps.get_model("users", "User")

        # Check the app label
        app_label = model_class._meta.app_label

        print(f"App Label: {app_label}")
        return Response("test view")

    def post(self, request, *args, **kwargs):
        return Response("test view")
