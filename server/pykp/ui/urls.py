from django.urls import path
from pykp.ui import views

urlpatterns = [
        path("", views.homepage)
]
