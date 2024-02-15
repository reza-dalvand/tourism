from django.urls import include, path
from rest_framework import routers

from apps.comments.api.v1.apis.comments import CommentApi

router = routers.DefaultRouter()
router.register("", CommentApi, basename="comments")

urlpatterns = [
    path("", include(router.urls)),
]
