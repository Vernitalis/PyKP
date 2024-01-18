from django.urls import path
from pykp.scraper import views

urlpatterns = [
    path("AddStation", views.add_station),
]
