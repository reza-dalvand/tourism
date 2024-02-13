import pytest

from apps.tests.users.setup import Setup
from apps.users.models import User


class TestsUsersManagers(Setup):
    def test_create_user(self):
        user = User.objects.create_user(mobile="09121234567")
        assert user.mobile == "09121234567"
        assert user.is_staff is False
        assert user.is_superuser is False
        with pytest.raises(TypeError):
            User.objects.create_user()

        with pytest.raises(ValueError):
            User.objects.create_user(mobile="")

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(mobile="09121234567", email="test@test.com", password="test")
        assert admin_user.mobile == "09121234567"
        assert admin_user.email == "test@test.com"
        assert admin_user.is_active is True
        assert admin_user.is_staff is True
        assert admin_user.is_superuser is True
        try:
            assert admin_user.username is None
        except AttributeError:
            pass
        with pytest.raises(ValueError):
            User.objects.create_superuser(
                mobile="09121234567", email="test@test.com", password="test", is_superuser=False
            )
