from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django.views.generic.edit import DeleteView
from weatherapp.weather.forms import LocationForm
from weatherapp.weather.models import Location
import requests
# Create your views here.

class LocationListView(ListView):
    model =  Location
    context_object_name = "locations"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        zipcode = self.request.GET.get("zipcode")
        weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&units=imperial&appid=655dfc390726be35679ee1f171b45301').json()
        if weather_data['cod'] == 200:
            context["data"] = weather_data
        return context
    
class LocationDeleteView(DeleteView):
    model = Location
    success_url = reverse_lazy('weather:weather')

class LocationSaveView(FormView):
    form_class = LocationForm
    success_url = reverse_lazy('weather:weather')
    def form_valid(self, form):
        location = form.save(commit=False)
        if not Location.objects.filter(zipcode=location.zipcode).exists():
            location.save()
        return super().form_valid(form)