import pytest
from rest_framework import status
from setup import Setup

from apps.users.models import User


class TestProfile(Setup):
    @pytest.fixture
    def setup_data(self):
        mobile = "09151234567"
        self.api_client.post(self.auth_url, data={"mobile": mobile})
        self.user = User.objects.get(mobile=mobile)
        self.user.email = "test@example.com"
        self.user.save()
        self.api_client.force_authenticate(self.user)
        yield "setup_data"
        print("tear down...")

    def test_send_verify_email(self, setup_data):
        response = self.api_client.post(self.send_verify_email_url, data={"email": self.user.email})
        assert response.status_code == status.HTTP_200_OK

    def test_verify_email(self, setup_data):
        url = f"{self.verify_email_url}/{self.user.email}/{self.user.uuid}"
        response = self.api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_update_user_profile(self, setup_data):
        response = self.api_client.put(f"{self.update_profile_url}/{self.user.id}/", data={"first_name": "example"})
        assert response.status_code == status.HTTP_200_OK
