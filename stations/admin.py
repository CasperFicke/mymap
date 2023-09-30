# stations/admin.py

# django
#from django.contrib import admin
from django.contrib.gis import admin

# packages
from leaflet.admin import LeafletGeoAdmin

# local
from .models import WeatherStation

# register weatherstation
admin.site.register(WeatherStation, LeafletGeoAdmin)
