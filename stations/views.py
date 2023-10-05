# stations/views.py

# django
from django.shortcuts import render
from django.views.generic.base import TemplateView

# local
from .models import WeatherStation

# All stations map view
def all_stations(request):
  title    = 'Weatherstations'
  stations = WeatherStation.objects.all()
  context = {
    'title'    : title,
    'stations' : stations
  }
  return render(request,'stations/all_stations.html', context)

# Draw test view
def DrawtestView(request):
  title = 'drawtest'
  context = {
    'title': title,
  }
  return  render(request, 'stations/draw_test.html', context)
