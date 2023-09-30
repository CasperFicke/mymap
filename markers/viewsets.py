# markers/viewsets.py

from rest_framework import viewsets
from rest_framework_gis import filters

from markers.models import Marker, Area, Multiarea, Multiline
from markers.serializers import MarkerSerializer, AreaSerializer, MultiareaSerializer, MultilineSerializer

# Marker viewset
class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
  bbox_filter_field = "location"
  filter_backends   = (filters.InBBoxFilter,)
  queryset          = Marker.objects.all()
  serializer_class  = MarkerSerializer

# Area viewset
class AreaViewSet(viewsets.ReadOnlyModelViewSet):
  bbox_filter_field = "area"
  filter_backends   = (filters.InBBoxFilter,)
  queryset          = Area.objects.all()
  serializer_class  = AreaSerializer

# Multiarea viewset
class MultiareaViewSet(viewsets.ReadOnlyModelViewSet):
  bbox_filter_field = "areas"
  filter_backends   = (filters.InBBoxFilter,)
  queryset          = Multiarea.objects.all()
  serializer_class  = MultiareaSerializer

# Multiline viewset
class MultilineViewSet(viewsets.ReadOnlyModelViewSet):
  bbox_filter_field = "line"
  filter_backends   = (filters.InBBoxFilter,)
  queryset          = Multiline.objects.all()
  serializer_class  = MultilineSerializer