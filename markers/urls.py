# markers/urls.py

# django
from django.urls import path

# local
from .views import MarkersMapView, MarkersWFSView, MarkersafstandView

app_name = "markers"

urlpatterns = [
  path("map/"     , MarkersMapView.as_view()     , name="map"),
  path("wfs/"     , MarkersWFSView.as_view()     , name="wfs"),
  path("afstand/" , MarkersafstandView.as_view() , name="afstand"),
]