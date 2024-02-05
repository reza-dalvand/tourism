from django.urls import include, path
from rest_framework import routers

from .apis.hotel import HotelApi

router = routers.DefaultRouter()
router.register("", HotelApi, basename="hotels")

urlpatterns = [
    path("", include(router.urls)),
]
