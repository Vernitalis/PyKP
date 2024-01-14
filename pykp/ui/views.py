from django.shortcuts import render
from django.http import HttpRequest


def homepage(request: HttpRequest):
    context = {}
    return render(request, "index.html", context)
