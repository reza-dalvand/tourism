from datetime import datetime, timedelta

import pytest
from rest_framework import status

from apps.tests.users.test_setup import TestSetup
from apps.users.models import User
from apps.utils.generate_otp import check_expire_otp, generate_otp_code


class TestAuthentication(TestSetup):
    @pytest.fixture
    def setup_data(self):
        self.api_client.post(self.auth_url, data={"mobile": "09131234567"})
        yield "setup_data"
        print("tear down...")

    def test_auth(self):
        response = self.api_client.post(self.auth_url, data={"mobile": "09131234567"})
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_201_CREATED]

    def test_auth_with_bad_request(self, setup_data):
        response = self.api_client.post(self.auth_url, data={"mobile": ""})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_check_expire_otp(self, setup_data):
        response = self.api_client.post(self.auth_url, data={"mobile": "09131234567"})
        assert response.status_code == status.HTTP_409_CONFLICT


class TestVerifyAuthentication(TestSetup):
    @pytest.fixture
    def setup_data(self):
        self.api_client.post(self.auth_url, data={"mobile": "09141234567"})
        self.user = User.objects.get(mobile="09141234567")
        yield "setup_data"
        print("tear down...")

    def test_auth_verify(self, setup_data):
        self.user.otp = generate_otp_code()
        self.user.save()
        response = self.api_client.post(self.verify_auth_url, data={"code": self.user.otp})
        assert response.status_code == status.HTTP_200_OK

    def test_invalid_auth_verify(self, setup_data):
        response = self.api_client.post(self.verify_auth_url, data={"code": "invalid code"})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_otp_code_is_expired(self, setup_data):
        self.user.otp_create_time = datetime.now() - timedelta(seconds=125)
        self.user.save()
        assert check_expire_otp(self.user) is False


class TestProfile(TestSetup):
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
