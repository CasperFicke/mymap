# markers/models.py

# django
from django.contrib.gis.db import models

# marker model
class Marker(models.Model):
  name     = models.CharField(max_length=255)
  location = models.PointField()

  def __str__(self):
    return self.name

# area model
class Area(models.Model):
  name     = models.CharField(max_length=255)
  area     = models.PolygonField()

  def __str__(self):
    return self.name

# multiarea model
class Multiarea(models.Model):
  name     = models.CharField(max_length=255)
  areas    = models.MultiPolygonField()

  def __str__(self):
    return self.name

# multiline model
class Multiline(models.Model):
  name     = models.CharField(max_length=255)
  line     = models.MultiLineStringField()

  def __str__(self):
    return self.name