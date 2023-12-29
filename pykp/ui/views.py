# from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from pykp.shared.models import Location
import folium

def homepage(request: HttpRequest):
    mymap = folium.Map(location=[52.0, 19.0],
                       zoom_start=7,
                       tiles='https://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png',
                       attr='Map data: {attribution.OpenStreetMap} | Map style: &copy;'
                       ' <a href="https://www.OpenRailwayMap.org">OpenRailwayMap</a> '
                       '(<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
                       )
    locations = Location.objects.all()
    for l in locations:
        # custom_icon = folium.CustomIcon(icon_image='point.png',icon_size=(7, 7))
        folium.Marker(location=[l.lat, l.lon], icon=folium.Icon(color="green"), popup=l.name).add_to(mymap)
    response_body = mymap.get_root().render().encode()
    return HttpResponse(response_body)

