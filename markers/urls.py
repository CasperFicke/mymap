# markers/urls.py

# django
from django.urls import path

# local
from .views import (
  #MarkersMapView,
  MarkersWFSView,
  all_markersMapView,
  show_markerView,
  all_afstandenView)

app_name = "markers"

urlpatterns = [
  path("map/"               , all_markersMapView        , name="all-markers-map"),
  path("markers/<int:pk>"   , show_markerView           , name="show-marker"),
  path("wfs/"               , MarkersWFSView.as_view()  , name="wfs"),
  path("afstanden/"         , all_afstandenView         , name="all-afstanden"),
]