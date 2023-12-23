from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config.django import base
from config.django.base import DEBUG

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/<str:version>/", include("apps.api.urls", namespace="api")),
]

if DEBUG:
    urlpatterns += [
        path("rosetta/", include("rosetta.urls")),
        path("api-auth/", include("rest_framework.urls")),
    ] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
