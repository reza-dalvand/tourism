from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.admin import admin_users
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
    path("admin/", admin.site.urls),
    path("users/admin/", admin_users.urls),
    path("test/", TestView.as_view()),
    path("api/<str:version>/", include("apps.api.urls", namespace="api")),
    # todo: handel address for get token from hear or use api LoginOrRegister in user app
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

if DEBUG:
    urlpatterns += [
        path("rosetta/", include("rosetta.urls")),
        path("__debug__/", include("debug_toolbar.urls")),
        path("api-auth/", include("rest_framework.urls")),
        path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
    ] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
