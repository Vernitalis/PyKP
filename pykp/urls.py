from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("scraper/", include("pykp.scraper.urls")),
    path("geo/", include("pykp.geo.urls")),
    path("", include("pykp.ui.urls")),
]
