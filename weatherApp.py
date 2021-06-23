#!/bin/python3

# SHAPE AI PROJECT - Weather App

# IMPORTS
import requests
import json
from datetime import datetime

# Log last successful API request
def logFile(dataX):
    with open("logPrevious.txt", 'w') as f:
        f.write(dataX)

# MAIN
API_KEY = "6a77c115c0dcf78aaee28c8fe5e1776e"  # from a throwaway account (Obviously)
city = input("Enter a city name: ")
r = requests.get(
    f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
)
data = r.json()

if data['cod'] == 200:
    cityTemp = ((data['main']['temp']) - 273.15)
    weatherInfo = data['weather'][0]['description']
    humidityInfo = data['main']['humidity']
    windSpeed = data['wind']['speed']
    degree_sign = u"\N{DEGREE SIGN}"
    dataX = f'''\nWeather Stats for - {city.upper()} | {datetime.now().strftime("%d %b %Y | %I:%M:%S %p")}\n> Current temperature is: {round(cityTemp,2)}{degree_sign}C\n> Current weather desc  : {weatherInfo}\n> Current Humidity      : {humidityInfo}%\n> Current wind speed    : {windSpeed}kmph\n'''
    logFile(dataX)
    print(dataX)
else:
    print(data['message'])