from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.utils.send_email import send_email


# Create your views here.
class TestView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        send_email("python", "django", ["rdalvand2001@gmail.com"])
        return Response("test view")

    def post(self, request, *args, **kwargs):
        return Response("test view")
