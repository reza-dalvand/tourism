from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config.django import base

urlpatterns = [path("admin/", admin.site.urls), path("rosetta/", include("rosetta.urls"))]

urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
