# stations/forms.py

# django
from django import forms

# packages
from leaflet.forms.widgets import LeafletWidget

# local
from .models import WeatherStation

class WeatherStationForm(forms.ModelForm):

  class Meta:
    model   = WeatherStation
    widgets = {'geom': LeafletWidget()}
    fields  = ('name', 'geom')