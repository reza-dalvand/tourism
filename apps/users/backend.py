from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from apps.users.models import User


class MobileBackend(ModelBackend):
    """
    Custom backend for authentication with mobile numbers

    Parameters:
        - mobile: string

    Returns:
        -user: User object
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.using("users_db").get(mobile=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.using("users_db").get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
