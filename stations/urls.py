# stations/urs.py

# django
from django.urls import path

# local
from . import views

app_name = "stations"

urlpatterns = [
#  path("stations/"    , AllStationsView.as_view() , name="all-stations"),
  path("stations/"    , views.all_stations , name="all-stations"),
  path("drawtest/"    , views.DrawtestView , name="draw-test"),
]