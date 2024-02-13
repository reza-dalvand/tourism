import pytest
from model_bakery import baker
from rest_framework import status

from apps.tests.tours.setup import SetUp
from apps.tours.models import Tour, TourismCompany, TourReservation
from apps.users.models import User


class TestTourReservation(SetUp):
    @pytest.fixture
    def setup_data(self):
        print("setup...")
        self.user = baker.make(User)
        self.company = baker.make(TourismCompany, company_name="example")
        self.tour = baker.make(Tour, user=self.user, company_name=self.company)
        self.api_client.force_authenticate(self.user)
        self.data = {
            "company_name": self.company.company_name,
            "user": self.user.id,
            "tour": self.tour.id,
        }
        yield "setup_data"
        print("tear down...")

    def test_reserve_tour(self, setup_data):
        response = self.api_client.post(self.reserve_url, data=self.data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_create_reserve_with_invalid_data(self, setup_data):
        response = self.api_client.post(self.reserve_url, data={})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_reserve_with_invalid_date(self, setup_data):
        with pytest.raises(Exception) as e:
            self.data["exit_date"] = self.data.get("entry_date")
            self.api_client.post(self.reserve_url, data=self.data)

    def test_cancel_reservation(self, setup_data):
        self.reservation = baker.make(TourReservation, user=self.user, company_name=self.company, tour=self.tour)
        response = self.api_client.delete(f"{self.reserve_url}{self.reservation.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
