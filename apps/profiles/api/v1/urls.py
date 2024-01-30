from django.urls import path

from .apis.update_profile import UpdateProfile
from .apis.verify_email import SendVerifyEmail, VerifyEmail

urlpatterns = [
    path("send/email/", SendVerifyEmail.as_view(), name="send_email"),
    path("verify/<str:email>/<str:user_uuid>", VerifyEmail.as_view(), name="verify_email"),
    path("update/<int:pk>/", UpdateProfile.as_view(), name="update_profile"),
]
