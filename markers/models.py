# markers/models.py

# django
from django.contrib.gis.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.html import mark_safe

# abstracts from django extensions
from django_extensions.db.models import (
  TimeStampedModel,
	ActivatorModel 
)

# installed packages
import uuid

# marker model
class Marker(models.Model):
  name     = models.CharField(max_length=255)
  image    = models.ImageField(blank=True, null=True, upload_to='markers/')
  location = models.PointField()
  
  # create absolute url
  def get_absolute_url(self):
    return reverse('markers:show-marker', args=[self.id])
  # functie om object in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.name}'
  # functie om image in de admin web-pagina te kunnen presenteren
  def image_tag(self):
    if self.image != '':
      return mark_safe('<img src="%s%s" width="100" height="100" />' % (f'{settings.MEDIA_URL}', self.image))
  # override delete method to also delete the image
  def delete(self):
    self.image.delete()
    super().delete()

# areaType model
class AreaType(TimeStampedModel,ActivatorModel,models.Model):
  class Meta:
    ordering            = ['type']
    verbose_name        = 'area-type'
    verbose_name_plural = 'area types'
  # attributes
  type         = models.CharField('Area Type', max_length=100)
  beschrijving = models.TextField('Beschrijving', blank=True)
  
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.type

# area model
class Area(models.Model):
  class Meta:
    ordering            = ['name']
    verbose_name        = 'area'
    verbose_name_plural = 'areas'
  # attributes
  name         = models.CharField(max_length=255)
  beschrijving = models.TextField('Area beschrijving', blank=True, help_text='Beschrijving van de area')
  area         = models.PolygonField()
  # relaties
  type         = models.ForeignKey(AreaType, blank=True, null=True, on_delete=models.SET_NULL, related_name='areas')
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