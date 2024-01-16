from django.urls import path
from pykp.dataloader import views

urlpatterns = [
    path("AddStation", views.add_station),
]
