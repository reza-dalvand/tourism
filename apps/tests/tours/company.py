import pytest
from model_bakery import baker
from rest_framework import status
from setup import SetUp

from apps.tours.models import TourismCompany
from apps.users.models import User


class TestCompany(SetUp):
    @pytest.fixture
    def setup_data(self):
        print("setup...")
        self.user = baker.make(User, is_tour_company_owner=True)
        self.company = baker.make(TourismCompany, company_name="test")
        self.api_client.force_authenticate(self.user)
        yield "setup_data"
        print("tear down...")

    def test_create_company(self, setup_data):
        data = {
            "company_name": "example",
            "phone": "02112345678",
            "email": "example@example.com",
            "short_des": "example",
            "description": "example",
            "owner": 1,
        }
        response = self.api_client.post(self.company_url, data=data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_company_with_invalid_data(self, setup_data):
        response = self.api_client.post(self.company_url, data={})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_user_not_allowed_for_create_company(self, setup_data):
        self.user.is_tour_company_owner = False
        self.user.save()
        response = self.api_client.post(self.company_url, data={})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_remove_company(self, setup_data):
        response = self.api_client.delete(f"{self.company_url}{self.company.company_name}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_update_company(self, setup_data):
        response = self.api_client.patch(
            f"{self.company_url}{self.company.company_name}/", data={"email": "test@test.com"}
        )
        assert response.status_code == status.HTTP_200_OK
