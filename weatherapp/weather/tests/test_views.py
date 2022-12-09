from django.urls import reverse
from django.test import TestCase
from faker import Factory
from weatherapp.weather.models import Location
from .factories import LocationFactory

faker = Factory.create()


class LocationListViewTests(TestCase):

    valid_zipcode = '99501'
    invalid_zipcode = 'abcde'

    def setUp(self):
        LocationFactory.create_batch(11)

    def test_location_list_url_return_200(self):
        resp = self.client.get(reverse('weather:weather'))
        self.assertEqual(resp.status_code, 200)
    
    def test_location_list_count(self):
        resp = self.client.get(reverse('weather:weather'))
        self.assertEqual(resp.context['locations'].count(), 11)
    
    def test_data_is_empty_when_zipcode_param_not_provided(self):
        resp = self.client.get(reverse('weather:weather'))
        self.assertTrue('data' not in resp.context)
    
    def test_data_exists_when_zipcode_param_provided(self):
        resp = self.client.get(reverse('weather:weather'), {'zipcode': self.valid_zipcode})
        self.assertTrue('data' in resp.context)
    
    def test_data_code_returns_200_when_valid_zipcode_param_provided(self):
        resp = self.client.get(reverse('weather:weather'), {'zipcode': self.valid_zipcode})
        self.assertEqual(resp.context['data']['cod'], 200)
    
    def test_data_is_empty_when_invalid_zipcode_param_provided(self):
        resp = self.client.get(reverse('weather:weather'), {'zipcode': self.invalid_zipcode})
        self.assertTrue('data' not in resp.context)


class LocationSaveViewTest(TestCase):
    
    def setUp(self):
        Location.objects.create(title="Some title", zipcode="99501")
    
    def test_new_location_saved_when_zipcode_doesnt_exists(self):
        locations_count = Location.objects.count()
        response = self.client.post(reverse('weather:save-location'), {'title': "Some title", 'zipcode': "99502"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Location.objects.count(), locations_count + 1)
    
    def test_new_location_not_saved_when_zipcode_already_exists(self):
        locations_count = Location.objects.count()
        response = self.client.post(reverse('weather:save-location'), {'title': "Some title", 'zipcode': "99501"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Location.objects.count(), locations_count)