from django.urls import include, path

app_name = "api"
urlpatterns = [
    path("users/", include("apps.users.urls", namespace="users")),
    path("profiles/", include("apps.profiles.urls", namespace="profiles")),
    path("hotels/", include("apps.hotels.urls", namespace="hotels")),
]
