from django.conf import settings as conf_settings
from django.core.cache import cache

from users.models import Profile
from geopy.geocoders import Nominatim
import requests


def fetch_weather_api(lat, lon):
    ''' Fetch weather data for given latitude and longitude. '''
    MAIN_URL = 'http://api.openweathermap.org/data/2.5/weather?'
    API_KEY = conf_settings.WEATHER_KEY
    CITY = f'lat={lat}&lon={lon}'

    url = MAIN_URL + CITY + '&units=metric&appid=' + API_KEY
    response = requests.get(url).json()

    if response.get('main'):
        return {
            'temperature': round(response['main']['temp'], 1),
            'weather_icon': response['weather'][0]['icon'],
            'humidity': response['main']['humidity'],
            'wind': response['wind']['speed'],
            'pressure': response['main']['pressure'],
            'description': response['weather'][0]['description'],
            'main': response['weather'][0]['main'],
        }
    return None  # In case of an error


def weather_data(request):
    # Default: Moscow
    lat, lon = 55.75, 37.61

    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            if profile.latitude and profile.longitude:
                lat, lon = profile.latitude, profile.longitude
            elif profile.address:
                geolocator = Nominatim(user_agent="django_weather_app")
                location = geolocator.geocode(profile.address)
                if location:
                    lat, lon = location.latitude, location.longitude
        except Profile.DoesNotExist:
            pass

    new_weather_data = fetch_weather_api(lat, lon)
    return {'weather': new_weather_data}
