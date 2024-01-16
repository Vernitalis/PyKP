from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.serializers import serialize
from pykp.geo.models import Location


@csrf_exempt
@require_http_methods(["GET"])
def get_locations(request: HttpRequest):
    response_body = serialize(
        "geojson", Location.objects.all(), geometry_field="point"
    ).encode()
    return HttpResponse(response_body)
