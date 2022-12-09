from django.urls import path

from weatherapp.weather.views import (
    LocationListView,
    LocationDeleteView,
    LocationSaveView
)

app_name = "weather"
urlpatterns = [
    path("", view=LocationListView.as_view(), name="weather"),
    path("save-location", LocationSaveView.as_view(), name="save-location"),
    path('delete-location/<int:pk>', LocationDeleteView.as_view(), name='delete-location'),

]
