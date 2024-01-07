from django.shortcuts import render
from django.http import HttpRequest
from pykp.shared.models import Location
import folium
from folium.plugins import FastMarkerCluster


def homepage(request: HttpRequest):
    m = folium.Map(
        location=[52.0, 19.0],
        zoom_start=7,
        tiles="https://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png",
        attr="Map data: {attribution.OpenStreetMap} | Map style: &copy;"
        ' <a href="https://www.OpenRailwayMap.org">OpenRailwayMap</a> '
        '(<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',
    )
    locations = Location.objects.all()
    markers = [(location.lat, location.lon) for location in locations]
    cluster = FastMarkerCluster(data=markers)
    cluster.add_to(m)

    context = {"map": m._repr_html_()}
    return render(request, "index.html", context)
