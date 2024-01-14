from django.urls import path
from pykp.geo import views

urlpatterns = [
    path("FetchLocations", views.fetch_locations),
    path("GetLocations", views.get_locations),
]
