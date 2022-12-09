from rest_framework import serializers
from weatherapp.weather.models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["title", "zipcode"]
