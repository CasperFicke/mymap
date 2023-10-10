# markers/forms.py

# django
from django import forms
from django.forms import ModelForm, DateInput

# local
from .models import Marker

# Markerform
class MarkerForm(ModelForm):
  class Meta:
    model = Marker
    # fields = '__all__'
    fields = ('name', 'location')
    # exclude = ('slug', 'uuid', 'start_at', 'end_at', 'created')
    labels  = {
      'name'     : 'Naam van de marker',
      'location' : 'Locatie POINT (4.9 52.5)',
    }
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'name'     : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'marker naam...'}),
      'location' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'marker locatie...'}),
    }