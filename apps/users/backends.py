from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

User = get_user_model()


class MobileBackend(ModelBackend):
    """Override default approach authentication."""

    def authenticate(self, request, email=None, mobile=None, password=None, **kwargs):
        """
        Change default backend authentication.

        Args:
            request (request): Request object
            email (text): User email input
            mobile (text): User mobile number input
            password (text): User input password

        Returns:
            User instance
        """
        try:
            user = User.objects.get(Q(email__iexact=email) | Q(mobile__iexact=mobile))
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None
