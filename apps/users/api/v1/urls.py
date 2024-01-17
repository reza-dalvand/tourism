from django.urls import path

from apps.users.api.v1.apis.register import RegisterApi, VerifyRegistrationApi

urlpatterns = [
    path("verify-register/", VerifyRegistrationApi.as_view(), name="verify-register"),
    path("register/", RegisterApi.as_view(), name="register"),
]
