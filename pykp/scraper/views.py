import json
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from pykp.shared.models import Station
import logging

logger = logging.getLogger()


@csrf_exempt
@require_http_methods(["POST"])
def add_station(request: HttpRequest):
    try:
        body = request.body.decode()
        data = json.loads(body)
        Station.from_dict(data).save()
        return JsonResponse({"status": "SUCCESS"})
    except Exception as e:
        logger.error("{type}: {message}".format(type=type(e), message=e))
        response = JsonResponse(
            {"status": "ERROR", "message": "Couldn't load the JSON file"}
        )
        response.status_code = 400
        return response
