from django.urls import path
from pykp.dataloader import views

urlpatterns = [
    path("ImportStations", views.import_stations),
    path("AddStation", views.add_station),
    # path("FetchLocations", views.fetch_locations),
]
