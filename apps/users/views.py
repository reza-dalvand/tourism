from django.http import HttpResponse
from django.views import View

from apps.users.models import User


class TestView(View):
    def get(self, request):
        users = User.objects.create_user(mobile="09124567894")
        return HttpResponse(users)

    def post(self, request, *args, **kwargs):
        return HttpResponse("test view")
