from django import forms
from weatherapp.weather.models import Location

class LocationForm(forms.ModelForm):
    """Location form."""
    class Meta:
        model = Location
        fields = ['title','zipcode']