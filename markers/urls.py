# markers/urls.py

# django
from django.urls import path

# local
from .views import (
  MarkersWFSView,
  all_markersView,
  all_markersMapView,
  show_markerView,
  add_markerView,
  csv_markerView,
  save_markerView,
  show_markerView,
  all_afstandenView)

app_name = "markers"

urlpatterns = [
  path("markers/"                , all_markersView           , name='all-markers'),
  path("markers/map/"            , all_markersMapView        , name="all-markers-map"),
  path("markers/<int:marker_id>" , show_markerView           , name="show-marker"),
  path("markers/add"             , add_markerView            , name="add-marker"),
  path("markers/csv"             , csv_markerView            , name="csv-markers"),
  path("markers/savemarker"      , save_markerView           , name="save-marker"),
  path("wfs/"                    , MarkersWFSView.as_view()  , name="wfs"),
  path("afstanden/"              , all_afstandenView         , name="all-afstanden"),
]