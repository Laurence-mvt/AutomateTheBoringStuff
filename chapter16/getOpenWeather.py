#! python 3
# /usr/bin/env bash
# getOpenWeather.py - prints 2 day weather forecast for command line location

import sys, json, requests

APPID = '102fd9b6a57a705dcd914cefcacf8b4e'

# Compute location from command line arguments
if len(sys.argv) <2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')  # as required by the OpenWeatherMap API service
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = f"https://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&APPID={APPID}"
response = requests.get(url)
response.raise_for_status()

print(response)
# TODO: Load JSON data into a Python variable.
