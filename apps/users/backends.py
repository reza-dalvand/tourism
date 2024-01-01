from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class PhoneBackend(ModelBackend):
    """Override default approach authentication."""

    def authenticate(self, request, phone=None, password=None, **kwargs):
        """
        Change default backend authentication.

        Args:
            request (request): Request object
            phone (test): User phone input number
            password (text): User input password

        Returns:
            User instance
        """
        try:
            user = User.objects.get(phone__iexact=phone)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None
