import pytest
from model_bakery import baker
from rest_framework import status
from setup import SetUp

from apps.users.models import User


class TestHotel(SetUp):
    @pytest.fixture
    def setup_data(self):
        print("setup...")
        self.user = baker.make(User, is_hotel_owner=True)
        self.api_client.force_authenticate(self.user)
        yield "setup_data"
        print("tear down...")

    def test_hotel(self, setup_data):
        data = {
            "hotel_name": "test",
            "phone": "02112345678",
            "email": "example@example.com",
            "number_of_rooms": 5,
            "short_des": "test",
            "description": "test",
            "owner": 1,
        }
        response = self.api_client.post(self.hotel_url, data=data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_hotel_with_invalid_data(self, setup_data):
        response = self.api_client.post(self.hotel_url, data={})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_user_not_owner_for_create_hotel(self, setup_data):
        self.user.is_hotel_owner = False
        self.user.save()
        response = self.api_client.post(self.hotel_url, data={})
        assert response.status_code == status.HTTP_403_FORBIDDEN
