import pytest
from rest_framework.test import APIClient, APIRequestFactory


@pytest.mark.django_db(databases=["users_db"])
class Setup:
    def setup_method(self):
        self.api_client = APIClient()
        self.api_request = APIRequestFactory()
        self.prefix_url = "http://127.0.0.1:8000/api/v1"
        self.auth_url = f"{self.prefix_url}/users/auth/"
        self.verify_auth_url = f"{self.prefix_url}/users/auth/verify/"
        self.send_verify_email_url = f"{self.prefix_url}/profiles/send/email/"
        self.verify_email_url = f"{self.prefix_url}/profiles/verify"
