# from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
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

    response_body = m.get_root().render().encode()
    return HttpResponse(response_body)
