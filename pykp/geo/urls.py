from django.urls import path
from . import views

urlpatterns = [
    path("GetLocations", views.get_locations),
    path("GetOutline", views.get_outline),
]
