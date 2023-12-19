# from django.shortcuts import render
import json
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from pykp.shared.models import Station, Location
from overpy import Overpass

# TODO: Add some more error logging

@csrf_exempt
@require_http_methods(["POST"])
def add_station(request: HttpRequest):
    try:
        body = request.body.decode()
        data = json.loads(body)
        Station.from_dict(data).save()
        return HttpResponse(b"OK")
    except(Exception):
        return HttpResponseBadRequest(b"Couldn't load the JSON file")

@csrf_exempt
@require_http_methods(["POST"])
def import_stations(request: HttpRequest):
    try:
        body = request.body.decode()
        data = json.loads(body)
        print(data)
        stations_list = [Station.from_dict(s) for s in data]
        Station.objects.bulk_create(stations_list)
        return HttpResponse(b"OK")
    except Exception as e:
        print(e)
        return HttpResponseBadRequest(b"Couldn't load the JSON file")

@csrf_exempt
@require_http_methods(["GET"])
def fetch_locations(request: HttpRequest):
    overpass_api = Overpass()
    query = """
        [out:json];
        area["name"="Polska"]->.boundaryarea;
        (
        node(area.boundaryarea)
          ["railway"="halt"];
        node(area.boundaryarea)
          ["railway"="station"];
        );
        out;
    """
    try:
        query_response = overpass_api.query(query)
        locations = []
        for node in query_response.nodes:
            try:
                locations.append(Location(name=node.tags["name"], lat=node.lat, lon=node.lon, type=node.tags["railway"], id=node.id))
            except:
                pass
        Location.objects.bulk_create(locations)
        return HttpResponse(b"OK")
    except Exception as e:
        print(e)
        return HttpResponseBadRequest(b"A problem with fetching has occured")
