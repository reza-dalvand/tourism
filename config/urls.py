from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.users.views import TestView
from config.django import base
from config.django.base import DEBUG

schema_view = get_schema_view(
    openapi.Info(
        title="Documents API",
        default_version="v1",
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)

urlpatterns = [
    path("test/", TestView.as_view()),
    path("api/<str:version>/", include("apps.api.urls", namespace="api")),
] + i18n_patterns(path("admin/", admin.site.urls))

if DEBUG:
    urlpatterns += [
        path("rosetta/", include("rosetta.urls")),
        path("__debug__/", include("debug_toolbar.urls")),
        path("api-auth/", include("rest_framework.urls")),
        path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
    ] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
