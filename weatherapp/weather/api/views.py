from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from weatherapp.weather.models import Location
from .serializers import LocationSerializer

class LocationViewSet(ModelViewSet):
    """
    A viewset for viewing and editing location instances.
    """
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    search_fields = ['zipcode']
    filter_backends = (SearchFilter,)
