from django.urls import include, path
from rest_framework import routers

from .apis.hotel import HotelApi
from .apis.reservation import HotelReservation
from .apis.room import RoomApi

router = routers.DefaultRouter()
router.register("reservation", HotelReservation, basename="reservations")
router.register("rooms", RoomApi, basename="rooms")
router.register("", HotelApi, basename="hotels")

urlpatterns = [
    path("", include(router.urls)),
]
