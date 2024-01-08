from django.shortcuts import render
from django.http import HttpRequest
# from pykp.shared.models import Location


def homepage(request: HttpRequest):
    # locations = Location.objects.all()
    context = {}
    return render(request, "index.html", context)
