from django.urls import include, path
from rest_framework import routers

from .apis.company import TourismCompanyApi

router = routers.DefaultRouter()
router.register("company", TourismCompanyApi, basename="company")

urlpatterns = [
    path("", include(router.urls)),
]
