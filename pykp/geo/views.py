from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.gis.geos import Point
from pykp.geo.models import Location
from overpy import Overpass


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
            locations.append(
                Location(
                    name=node.tags["name"],
                    point=Point([node.lon, node.lat]),
                    type=node.tags["railway"],
                    id=node.id,
                )
            )
        Location.objects.bulk_create(locations)
        return HttpResponse(b"OK")
    except Exception as e:
        print(e)
        return HttpResponseBadRequest(b"A problem with fetching has occured")
