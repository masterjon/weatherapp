from django.test import TestCase

from .factories import LocationFactory


class VideoModelTest(TestCase):

    def setUp(self):
        self.location = LocationFactory.create()

    def test_string_representation(self):
        self.assertEqual(str(self.location), self.location.title)
