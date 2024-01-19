from django.urls import path

from .apis.authentication import LoginOrRegisterApi
from .apis.verify import VerifyOtpApi

urlpatterns = [
    path("auth/", LoginOrRegisterApi.as_view(), name="login_or_register"),
    path("auth/verify/", VerifyOtpApi.as_view(), name="verify-auth"),
]
