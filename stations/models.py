# stations/models.py

# django
from django.db import models
from django.contrib.gis.db import models as gismodels

# Weatherstation model
class WeatherStation(gismodels.Model):
  wmoid       = models.IntegerField(primary_key=True)
  name        = models.CharField(max_length=256)
  picture     = models.ImageField(blank=True, null=True, upload_to="stations/")
  description = models.TextField(blank=True, null=True)
  geom        = gismodels.PointField()
  objects     = gismodels.Manager()

  @property
  def popupContent(self):
    return '<img src="{}" /><p>{}</p>'.format(
        self.picture.url,
        self.description)

  def __str__(self):
    return self.name

