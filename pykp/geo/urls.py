from django.urls import path
from pykp.geo import views

urlpatterns = [
    path("GetLocations", views.get_locations),
]
