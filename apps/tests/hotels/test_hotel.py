import pytest
from model_bakery import baker
from rest_framework import status

from apps.hotels.models import Hotel
from apps.tests.hotels.setup import SetUp
from apps.users.models import User


class TestHotel(SetUp):
    @pytest.fixture
    def setup_data(self):
        print("setup...")
        self.user = baker.make(User, is_hotel_owner=True)
        self.hotel = baker.make(Hotel, hotel_name="test")
        self.api_client.force_authenticate(self.user)
        yield "setup_data"
        print("tear down...")

    def test_create_hotel(self, setup_data):
        data = {
            "hotel_name": "example",
            "phone": "02112345678",
            "email": "example@example.com",
            "number_of_rooms": 5,
            "short_des": "example",
            "description": "example",
            "owner": 1,
        }
        response = self.api_client.post(self.hotel_url, data=data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_create_hotel_with_invalid_data(self, setup_data):
        response = self.api_client.post(self.hotel_url, data={})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_user_not_allowed_for_create_hotel(self, setup_data):
        self.user.is_hotel_owner = False
        self.user.save()
        response = self.api_client.post(self.hotel_url, data={})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_remove_hotel(self, setup_data):
        response = self.api_client.delete(f"{self.hotel_url}{self.hotel.hotel_name}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_update_hotel(self, setup_data):
        response = self.api_client.patch(f"{self.hotel_url}{self.hotel.hotel_name}/", data={"email": "test@test.com"})
        assert response.status_code == status.HTTP_200_OK
