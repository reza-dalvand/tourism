from django.http import HttpResponse
from django.views import View

from apps.users.models import User


class TestView(View):
    def get(self, request):
        users = User.objects.using("users_db").get(mobile="09121234567")
        return HttpResponse(users)

    def post(self, request, *args, **kwargs):
        return HttpResponse("test view")
