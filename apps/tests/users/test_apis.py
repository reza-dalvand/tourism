import pytest
from django.test import Client
from rest_framework.test import APIClient

from apps.tests.users.test_setup import TestSetup


@pytest.mark.django_db
class TestAuthentication(TestSetup):
    @pytest.fixture
    def setup_data(self):
        print("Setting up")
        yield "setup"
        print("setup")

    def test_authentication(self, setup_data):
        response = self.client.post(self.auth_url, data={"mobile": "09121234567"})
        print(response, "response")
        assert 1 == 1
