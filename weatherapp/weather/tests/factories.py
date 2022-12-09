from factory import Faker
from factory.django import DjangoModelFactory
from weatherapp.weather.models import Location


class LocationFactory(DjangoModelFactory):

    title = Faker("sentence")
    zipcode = Faker("postcode")

    class Meta:
        model = Location
