import json
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from pykp.shared.models import Station

# TODO: Add some more error logging


@csrf_exempt
@require_http_methods(["POST"])
def add_station(request: HttpRequest):
    try:
        body = request.body.decode()
        data = json.loads(body)
        Station.from_dict(data).save()
        return HttpResponse(b"OK")
    except Exception:
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
