# markers/urls.py

# django
from django.urls import path

# local
from .views import (
  #MarkersMapView,
  MarkersWFSView,
  all_markersMapView,
  all_markersView,
  show_markerView,
  all_afstandenView)

app_name = "markers"

urlpatterns = [
  path("markers/"                , all_markersView           , name='all-markers'),
  path("markers/map/"            , all_markersMapView        , name="all-markers-map"),
  path("markers/<int:marker_id>" , show_markerView           , name="show-marker"),
  path("wfs/"                    , MarkersWFSView.as_view()  , name="wfs"),
  path("afstanden/"              , all_afstandenView         , name="all-afstanden"),
]