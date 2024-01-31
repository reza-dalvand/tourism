from django.http import HttpResponse
from django.views import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User


class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.using("custom_db").get(mobile="09121234567")
        return Response(users)

    def post(self, request, *args, **kwargs):
        return Response("test view")
