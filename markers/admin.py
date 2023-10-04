# markers/admin.py

# django
from django.contrib.gis import admin

# local
from .models import Marker, Area, Multiarea, Multiline

class LocationAdmin(admin.OSMGeoAdmin):
  default_lat  = 52.5
  default_lon  = 4.5
  default_zoom = 12

# marker model
@admin.register(Marker)
class MarkerAdmin(admin.GISModelAdmin):
  list_display = ('name', 'location', 'image_tag', )
  gis_widget_kwargs = {
    'attrs':{
      'default_lat': 52.5,
      'default_lon': 4.95,
      'default_zoom': 12,
    },
  }

# area model
@admin.register(Area)
class AreaAdmin(admin.GISModelAdmin):
  list_display = ("name", "area")
  gis_widget_kwargs = {
    'attrs':{
      'default_lat': 52.5,
      'default_lon': 4.95,
      'default_zoom': 14,
    },
  }

# multiarea model
@admin.register(Multiarea)
class MultiareaAdmin(admin.GISModelAdmin):
  list_display = ("name", "areas")
  gis_widget_kwargs = {
    'attrs':{
      'default_lat': 52.5,
      'default_lon': 4.95,
      'default_zoom': 12,
    },
  }

# multiline model
@admin.register(Multiline)
class AreaAdmin(admin.GISModelAdmin):
  list_display = ("name", "line")
  gis_widget_kwargs = {
    'attrs':{
      'default_lat': 52.5,
      'default_lon': 4.95,
      'default_zoom': 12,
    },
  }