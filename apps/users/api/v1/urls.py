from django.urls import path

from .apis.authentication import LoginOrRegisterApi, VerifyOtpApi

urlpatterns = [
    path("auth/", LoginOrRegisterApi.as_view(), name="register"),
    path("auth/verify/", VerifyOtpApi.as_view(), name="verify-register"),
]
