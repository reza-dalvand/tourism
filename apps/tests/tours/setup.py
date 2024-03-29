import pytest
from rest_framework.test import APIClient, APIRequestFactory


@pytest.mark.django_db(databases=["custom_db"])
class SetUp:
    def setup_method(self):
        self.api_client = APIClient()
        self.api_request = APIRequestFactory()
        self.prefix_url = "http://127.0.0.1:8000/api/v1"
        self.auth_url = f"{self.prefix_url}/users/auth/"
        self.tour_url = f"{self.prefix_url}/tours/"
        self.company_url = f"{self.prefix_url}/tours/companies/"
        self.reserve_url = f"{self.prefix_url}/tours/reservation/"
