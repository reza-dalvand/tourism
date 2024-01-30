import uuid

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User
from apps.utils.send_email import send_email


class SendVerifyEmail(APIView):
    """
    Send email verification link

    Parameters:
        -email
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        prefix = f"Click on activate link http://127.0.0.1:8000/api/{request.version}"
        message = f"{prefix}/profiles/verify/{user.email}/{user.uuid}"
        # todo: send email with celery
        send_email("Activate Email", message, [user.email])
        user.uuid = uuid.uuid4()
        user.save()
        return Response(data="Email was send", status=status.HTTP_200_OK)


class VerifyEmail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user_uuid = kwargs.get("user_uuid")
        user = get_object_or_404(User, uuid=user_uuid)
        user.email_is_verified = True
        user.save()
        return Response(data="Email was verified", status=status.HTTP_200_OK)
