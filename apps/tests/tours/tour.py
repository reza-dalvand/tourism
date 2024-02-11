from datetime import datetime, timedelta

import pytest
from model_bakery import baker
from rest_framework import status
from setup import SetUp

from apps.tours.models import Tour, TourismCompany
from apps.users.models import User


class TestTour(SetUp):
    @pytest.fixture
    def setup_data(self):
        print("setup...")
        self.user = baker.make(User, is_tourism_company_owner=True)
        self.company = baker.make(TourismCompany, company_name="test")
        self.tour = baker.make(Tour, user=self.user, company_name=self.company)
        self.api_client.force_authenticate(self.user)
        yield "setup_data"
        print("tear down...")

    def test_create_tour(self, setup_data):
        data = {
            "company_name": self.company.company_name,
            "user": self.user.id,
            "title": "example2",
            "start_date": datetime.now(),
            "end_date": datetime.now() + timedelta(days=3),
            "short_des": "test",
            "description": "test",
            "price": 100000,
            "capacity": 30,
        }
        response = self.api_client.post(self.tour_url, data=data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_create_tour_with_invalid_data(self, setup_data):
        response = self.api_client.post(self.tour_url, data={})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_user_not_allowed_for_create_tour(self, setup_data):
        self.user.is_tourism_company_owner = False
        self.user.save()
        response = self.api_client.post(self.tour_url, data={})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_remove_tour(self, setup_data):
        response = self.api_client.delete(f"{self.tour_url}{self.tour.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_update_tour(self, setup_data):
        response = self.api_client.patch(f"{self.tour_url}{self.tour.id}/", data={"title": "example"})
        assert response.status_code == status.HTTP_200_OK
