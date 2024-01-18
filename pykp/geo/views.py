from django.http import HttpRequest, HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.serializers import serialize
from django.contrib.gis.geos import GEOSGeometry

# from django.db.models.functions import Now
from .models import Location, Outline
import requests
from datetime import datetime, timezone


def refresh_outline(osm_id):
    url = "https://polygons.openstreetmap.fr/get_geojson.py"
    params = {"id": osm_id, "params": 0}
    try:
        outline = Outline.objects.get(osm_relation_id=osm_id)
        delta = (datetime.now(timezone.utc) - outline.last_update).total_seconds()
        if delta < (24 * 3600):
            return outline
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.HTTPError:
            return outline
        else:
            polygon = GEOSGeometry(response.text)
            outline.polygon = polygon
    except Outline.DoesNotExist:
        response = requests.get(url, params=params)
        response.raise_for_status()
        polygon = GEOSGeometry(response.text)
        outline = Outline(osm_relation_id=osm_id, polygon=polygon)
    outline.save()
    return outline


@csrf_exempt
@require_http_methods(["GET"])
def get_locations(request: HttpRequest):
    response_body = serialize(
        "geojson", Location.objects.all(), geometry_field="point"
    ).encode()
    return HttpResponse(response_body)


@csrf_exempt
@require_http_methods(["GET"])
def get_outline(request: HttpRequest):
    pl_id = 49715
    try:
        outline = refresh_outline(pl_id)
        response_body = serialize(
            "geojson",
            [
                outline,
            ],
            geometry_field="polygon",
        ).encode()
        return HttpResponse(response_body)
    except Exception:
        return HttpResponseServerError(b"ERROR")
