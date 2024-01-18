from django.urls import path
from . import views

urlpatterns = [
    path("AddStation", views.add_station),
]
