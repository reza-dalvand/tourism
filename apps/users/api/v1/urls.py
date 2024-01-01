from django.urls import path

from .apis.login import LoginApi
from .apis.register import RegisterApi

urlpatterns = [
    path("register/", RegisterApi.as_view(), name="register"),
    path("login/", LoginApi.as_view(), name="login"),
]
