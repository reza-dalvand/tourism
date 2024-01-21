from django.http import HttpResponse
from django.views import View

from apps.users.models import User


# Create your views here.
class TestView(View):
    def get(self, request):
        users = User.objects.all()
        return HttpResponse(users)

    def post(self, request, *args, **kwargs):
        return HttpResponse("test view")
