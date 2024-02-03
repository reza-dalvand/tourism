from django.urls import include, path
from rest_framework import routers

from .apis.hotel import HotelApi
from .apis.reserve import HotelReservation
from .apis.room import RoomApi

router = routers.DefaultRouter()
router.register("rooms", RoomApi, basename="rooms")
router.register("", HotelApi, basename="hotels")

urlpatterns = [
    path("reserve/", HotelReservation.as_view(), name="reserve"),
    path("", include(router.urls)),
]
