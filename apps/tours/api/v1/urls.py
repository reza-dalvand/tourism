from django.urls import include, path
from rest_framework import routers

from .apis.company import TourismCompanyApi
from .apis.tour import TourApi

router = routers.DefaultRouter()
router.register("companies", TourismCompanyApi, basename="company")
router.register("", TourApi, basename="all-tours")

urlpatterns = [
    path("", include(router.urls)),
]
