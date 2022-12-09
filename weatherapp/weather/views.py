from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django.views.generic.edit import DeleteView
from weatherapp.weather.forms import LocationForm
from weatherapp.weather.models import Location
import requests
# Create your views here.

class LocationListView(ListView):
    """Location list view.

    Handle retreiving the list of locations and fetching weather data from api.openweathermap.org
    """
    model =  Location
    context_object_name = "locations"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        zipcode = self.request.GET.get("zipcode")
        weather_request_url = f'{settings.WEATHER_API_PROVIDER_BASE_URL}weather?zip={zipcode},us&units=imperial&appid={settings.WEATHER_API_PROVIDER_APP_ID}'
        weather_data = requests.get(weather_request_url).json()
        if weather_data['cod'] == 200:
            context["data"] = weather_data
        return context
    
class LocationDeleteView(DeleteView):
    """Location delete view.

    Handles deleting a location
    """
    model = Location
    success_url = reverse_lazy('weather:weather')

class LocationSaveView(FormView):
    """Location save view.

    Handles saving a location when the zipcode doesnt already exists.
    """
    form_class = LocationForm
    success_url = reverse_lazy('weather:weather')
    def form_valid(self, form):
        location = form.save(commit=False)
        if not Location.objects.filter(zipcode=location.zipcode).exists():
            location.save()
        return super().form_valid(form)