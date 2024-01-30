from django.urls import path

from .apis.verify_email import SendVerifyEmail, VerifyEmail

urlpatterns = [
    path("send/email/", SendVerifyEmail.as_view(), name="send_email"),
    path("verify/<str:email>/<str:user_uuid>", VerifyEmail.as_view(), name="verify_email"),
]
