from django.urls import path

from .apis.auth_verify import VerifyOtpApi
from .apis.authentication import LoginOrRegisterApi

urlpatterns = [
    path("auth/", LoginOrRegisterApi.as_view(), name="login_or_register"),
    path("auth/verify/", VerifyOtpApi.as_view(), name="verify-auth"),
]
