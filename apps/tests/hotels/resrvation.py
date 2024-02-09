import datetime
from datetime import datetime, timedelta

import pytest
from model_bakery import baker
from rest_framework import status
from setup import SetUp

from apps.hotels.models import Hotel, Reservation, Room
from apps.users.models import User


class TestHotelReservation(SetUp):
    @pytest.fixture
    def setup_data(self):
        print("setup...")
        self.user = baker.make(User)
        self.hotel = baker.make(Hotel)
        self.room = baker.make(Room, owner=self.user, hotel=self.hotel)
        self.api_client.force_authenticate(self.user)
        self.data = {
            "hotel": self.hotel.hotel_name,
            "user": self.user.id,
            "room": self.room.room_id,
            "entry_date": datetime.now(),
            "exit_date": datetime.now() + timedelta(days=2),
        }
        yield "setup_data"
        print("tear down...")

    def test_create_room(self, setup_data):
        response = self.api_client.post(self.reserve_url, data=self.data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_reserve_with_invalid_data(self, setup_data):
        response = self.api_client.post(self.reserve_url, data={})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_reserve_with_invalid_date(self, setup_data):
        with pytest.raises(Exception) as e:
            self.data["exit_date"] = self.data.get("entry_date")
            self.api_client.post(self.reserve_url, data=self.data)

    def test_cancel_reservation(self, setup_data):
        room = baker.make(Room, owner=self.user, hotel=self.hotel)
        self.reservation = baker.make(Reservation, user=self.user, hotel=self.hotel, room=room)
        response = self.api_client.delete(f"{self.reserve_url}{self.reservation.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
