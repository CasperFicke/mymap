# markers/views.py

# django
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import generic
from django.core.serializers import serialize

from django.contrib.gis.geos import Point, fromstr
from django.contrib.gis.db.models.functions import Distance

# packages
from gisserver.features import FeatureType, ServiceDescription
from gisserver.geometries import CRS, WGS84
from gisserver.views import WFSView

# local
from .models import Marker, Area, Multiarea, Multiline

RD_NEW = CRS.from_srid(28992)
WGS_84 = CRS.from_srid(4326)

latitude  = 52.507
longitude = 4.954
user_location = Point(longitude, latitude, srid=4326)

# Markers Map view
class MarkersMapView(TemplateView):
  template_name = "markers/map.html"

# Markers afstand
class MarkersafstandView(generic.ListView):
  model               = Marker
  context_object_name = 'markers'
  queryset            = Marker.objects.annotate(
    distance = Distance('location', user_location)
  ).order_by('distance')[0:6] # maximaal de 6 dichtsbijzijnde
  template_name       = 'markers/afstanden.html'

# Markers WFS
class MarkersWFSView(WFSView):
  """An simple view that uses the WFSView against our test model."""

  xml_namespace = "http://example.org/gisserver"

  # The service metadata
  service_description = ServiceDescription(
    title          = "Markers",
    abstract       = "Unittesting",
    keywords       = ["django-gisserver"],
    provider_name  = "Datalab",
    provider_site  = "https://purmerend.nl/in-purmerend-en-beemster/datalab-purmerend",
    contact_person = "datalab Purmerend",
  )

  # Each Django model is listed here as a feature.
  feature_types = [
    FeatureType(
      Marker.objects.all(),
      fields    = "__all__",
      other_crs = [RD_NEW]
    ),
    FeatureType(
      Area.objects.all(),
      fields    = "__all__",
      other_crs = [RD_NEW]
    ),
    FeatureType(
      Multiarea.objects.all(),
      fields    = "__all__",
      other_crs = [RD_NEW]
    ),
    FeatureType(
      Multiline.objects.all(),
      fields    = "__all__",
      other_crs = [RD_NEW]
    ),
  ]
