from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where phone is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone, email, password, **extra_fields):
        """
        Create and save a user with the given phone, email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        if not phone:
            raise ValueError(_("The phone number must be set"))
        email = self.normalize_email(email)
        user = self.model(phone=phone, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given phone, email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone, email, password, **extra_fields)
