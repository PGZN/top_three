import forecastio
from geopy.geocoders import Nominatim
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_forecast(address):
	api_key = os.environ['WEATHER_API']
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	lat = location.latitude
	lng = location.longitude
	forecast = forecastio.load_forecast(api_key, lat, lng).currently()
	return ("The current forecast for {} is {} and {}°, with {}% chance of rain." \
		.format(location, forecast.summary, forecast.temperature, forecast.precipProbability * 100))