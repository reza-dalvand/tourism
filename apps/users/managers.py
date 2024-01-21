from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

DEFAULT_USER_DB = "users"


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where mobile is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, mobile, **extra_fields):
        if not mobile:
            raise ValueError("The mobile field must be set")
        user = self.model(mobile=mobile, **extra_fields)
        user.set_unusable_password()
        user.save(using=DEFAULT_USER_DB)
        return user

    def create_superuser(self, email, password, mobile, **extra_fields):
        """
        Create and save a SuperUser with the given mobile, email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        user = self.model(mobile=mobile, email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=DEFAULT_USER_DB)
        return user
