# markers/serializers.py

# plugins
from rest_framework_gis import serializers

# local
from markers.models import Marker, Area, Multiarea, Multiline

# Marker serializer
class MarkerSerializer(serializers.GeoFeatureModelSerializer):
  class Meta:
    fields = ("id", "name")
    geo_field = "location"
    model = Marker

# Area serializer
class AreaSerializer(serializers.GeoFeatureModelSerializer):
  class Meta:
    fields = ("id", "name")
    geo_field = "area"
    model = Area

# Multiarea serializer
class MultiareaSerializer(serializers.GeoFeatureModelSerializer):
  class Meta:
    fields = ("id", "name")
    geo_field = "areas"
    model = Multiarea

# Multiline serializer
class MultilineSerializer(serializers.GeoFeatureModelSerializer):
  class Meta:
    fields = ("id", "name")
    geo_field = "line"
    model = Multiline