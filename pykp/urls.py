from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("rest/", include("pykp.rest.urls")),
    path("", include("pykp.ui.urls")),
]
