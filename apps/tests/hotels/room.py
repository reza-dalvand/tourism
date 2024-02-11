import pytest
from model_bakery import baker
from rest_framework import status
from setup import SetUp

from apps.hotels.models import Hotel, Room
from apps.users.models import User


class TestRoom(SetUp):
    @pytest.fixture
    def setup_data(self):
        print("setup...")
        self.user = baker.make(User, is_hotel_owner=True)
        self.hotel = baker.make(Hotel, hotel_name="example")
        self.room = baker.make(Room, owner=self.user, hotel=self.hotel)
        self.api_client.force_authenticate(self.user)
        yield "setup_data"
        print("tear down...")

    def test_create_room(self, setup_data):
        data = {
            "hotel": self.hotel.hotel_name,
            "number_of_bed": 2,
            "has_wifi": False,
            "has_bathroom": True,
            "owner": self.user.id,
            "price": "250000",
        }
        response = self.api_client.post(self.room_url, data=data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_create_room_with_invalid_data(self, setup_data):
        response = self.api_client.post(self.room_url, data={})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_user_not_allowed_for_create_room(self, setup_data):
        self.user.is_hotel_owner = False
        self.user.save()
        response = self.api_client.post(self.room_url, data={})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_remove_room(self, setup_data):
        response = self.api_client.delete(f"{self.room_url}{self.room.room_id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_update_room(self, setup_data):
        response = self.api_client.patch(f"{self.room_url}{self.room.room_id}/", data={"has_wifi": True})
        assert response.status_code == status.HTTP_200_OK
