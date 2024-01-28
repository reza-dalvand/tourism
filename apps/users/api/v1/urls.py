from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .apis.auth_verify import VerifyOtpApi
from .apis.authentication import LoginOrRegisterApi

urlpatterns = [
    path("auth/", LoginOrRegisterApi.as_view(), name="authentication"),
    path("auth/verify/", VerifyOtpApi.as_view(), name="verify_auth"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
