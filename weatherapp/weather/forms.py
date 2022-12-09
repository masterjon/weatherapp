from django import forms
from weatherapp.weather.models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['title','zipcode']