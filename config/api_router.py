from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from weatherapp.users.api.views import UserViewSet
from weatherapp.weather.api.views import LocationViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("locations", LocationViewSet)


app_name = "api"
urlpatterns = router.urls
