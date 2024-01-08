from django.urls import path
from pykp.rest import views

urlpatterns = [
    path("ImportStations", views.import_stations),
    path("AddStation", views.add_station),
    # path("FetchLocations", views.fetch_locations),
]
