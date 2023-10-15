# markers/views.py

# django
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse, HttpResponseRedirect, request
from django.core.serializers import serialize

from django.contrib.gis.geos import Point, fromstr
from django.contrib.gis.db.models.functions import Distance

# packages
from gisserver.features import FeatureType, ServiceDescription
from gisserver.geometries import CRS, WGS84
from gisserver.views import WFSView

# 
from datetime import date
import csv

# local
from .models import Marker, Area, Multiarea, Multiline
from .forms import MarkerForm

RD_NEW = CRS.from_srid(28992)
WGS_84 = CRS.from_srid(4326)

latitude  = 52.507
longitude = 4.954
user_location = Point(longitude, latitude, srid=4326)

# Markers Map view
#class MarkersMapView(TemplateView):
#  template_name = "markers/map.html"

# all markers view (lijst)
def all_markersView(request):
  title = 'All markers'
  markers = Marker.objects.annotate(
    distance = Distance('location', user_location)
  ).order_by('distance')
  context ={
    'title'   : title,
    'markers' : markers
  }
  return render(request, 'markers/all_markers.html', context)

# export markers to CSV
def csv_markerView(request):
  response= HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename=MarkersList_' + str(date.today()) + '.csv'
  # create CSV writer
  writer=csv.writer(response)
  # Select all markers to export
  markers_list = Marker.objects.all()
  # create first row with column headings
  writer.writerow(['Naam', 'Geocodering', 'Locatie'])
  # loop thru and output
  for marker in markers_list:
    writer.writerow([marker.name, marker.location])
  return response

# all markers map view
def all_markersMapView(request):
  title   = 'alle markers'
  markers = Marker.objects.all()
  areas   = Area.objects.all()
  context = {
    'title'   :  title,
    'markers' : markers,
    'areas'   : areas
  }
  return render(request, 'markers/map.html', context)

# show marker view
def show_markerView(request, marker_id):
  title = 'marker'
  try:
    marker = Marker.objects.get(id=marker_id)
    context = {
      'title'  : title,
      'marker' : marker
    }
    return render(request, 'markers/show_marker.html', context)
  except:
    raise Http404()

# add marker
@login_required
def add_markerView(request):
  title = 'Add Marker'
  if request.method == "POST":
    form = MarkerForm(request.POST)
    if form.is_valid():
      marker = form.save(commit=False)
      marker.save()
      messages.success(request, ("Marker " + marker.name + " has been added!"))
      return HttpResponseRedirect('/markers/markers/')
  else:
    form = MarkerForm
  context = {
    'title' : title,
    'form'  : form,
  }
  return render(request, 'markers/add_marker.html', context)

# Save marker to db
def save_markerView(request):
  marker_location = 'SRID=4326;POINT (4.8 52.7)'
  # add markerlocation to db
  m_location = Marker(
    name     = 'hallo',
    location = marker_location
  )
  m_location.save()
  return render(request, 'markers/afstanden.html')

# all afstanden map view
def all_afstandenView(request):
  title = 'Afstanden'
  markers = Marker.objects.annotate(
    distance = Distance('location', user_location)
  ).order_by('distance')[0:6] # maximaal de 6 dichtsbijzijnde
  context ={
    'title'   : title,
    'markers' : markers
  }
  return render(request, 'markers/afstanden.html', context)

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
