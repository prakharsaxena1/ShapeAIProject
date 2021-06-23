#!/bin/python3

# SHAPE AI PROJECT - Weather App(GUI)

# IMPORTS
import tkinter as tk
from tkinter import ttk
from tkinter.constants import LEFT, RIGHT
from datetime import datetime
import requests

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --

# MAIN
API_KEY = "6a77c115c0dcf78aaee28c8fe5e1776e" # from a throwaway account (Obviously)

# Log last successful API request
def logFile(dataX):
    with open("logPreviousGUI.txt", 'w') as f:
        f.write(dataX)

# Get data from API
def getDatafromAPI(city):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    )
    return r.json()

# Shows weather in
def showWeather():
    city = str(cityVariable.get())
    data = getDatafromAPI(city)
    if data['cod'] != 200:
        outLabel['text'] = data['message']
    else:
        cityTemp = ((data['main']['temp']) - 273.15)
        weatherInfo = data['weather'][0]['description']
        humidityInfo = data['main']['humidity']
        windSpeed = data['wind']['speed']
        degree_sign = u"\N{DEGREE SIGN}"
        dataX = f'''\nWeather Stats for - {city.upper()} | {datetime.now().strftime("%d %b %Y | %I:%M:%S %p")}\n\t Current temperature is: {round(cityTemp,2)}{degree_sign}C\n\t Current weather desc  : {weatherInfo}\n\t Current Humidity      : {humidityInfo}%\n\t Current wind speed    : {windSpeed}kmph\n'''
        outLabel['text'] = dataX
        logFile(dataX)

# Root window
root = tk.Tk()
root.geometry("580x420")
root.title("Weather App")
root.resizable(0, 0)

# Variables
cityVariable = tk.StringVar()

# Window title
titleLabel = ttk.Label(root, padding=5, text="Weather App")
titleLabel.config(font=("Comic Sans MS", 40))
titleLabel.grid(row=0, column=0, padx=(5), pady=(5), columnspan=4)

# City Label
cityNameLabel = ttk.Label(root, padding=5, text="City")
cityNameLabel.grid(row=1, column=0, padx=(5), pady=(5), ipadx=(5), ipady=(5), columnspan=2)
cityNameLabel.config(font=("Comic Sans MS", 16))

# Output Label
outLabel = ttk.Label(root, padding=5, text=" ")
outLabel.config(font=("Comic Sans MS", 15))
outLabel.grid(row=3, column=0, padx=(10), pady=(10), columnspan=4)

# City Entry
cityEntry = ttk.Entry(root, textvariable=cityVariable, width=50)
cityEntry.grid(row=1, column=2, padx=(10), pady=(10), ipadx=(10), ipady=(10), columnspan=2)
cityEntry.config(font=("Comic Sans MS", 16))

# Show weather button
showWeatherBtn = tk.Button(root, text="Report weather", command=showWeather)
showWeatherBtn.grid(row=2, column=0, padx=(10), pady=(10), ipadx=(10), ipady=(5), columnspan=4)
showWeatherBtn['font'] = ("Comic Sans MS", 15)

root.mainloop()