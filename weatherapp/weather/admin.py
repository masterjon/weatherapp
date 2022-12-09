from django.contrib import admin
from weatherapp.weather.models import Location

@admin.register(Location)
class ColoniaAdmin(admin.ModelAdmin):
    list_display = ['title', 'zipcode']
    search_fields = ['title', 'zipcode']