"""this script extracts data for London from the weatherappapi, converts into a pandas df. 
New cols for time stamp and conversion of temp to celsius are also created
"""

#import libraries
import requests
import json
import pandas as pd
from datetime import datetime

# Define the OpenWeatherMap API endpoint and parameters
api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_params = {
    "q": "London",  # Replace with the city of your choice
    "appid": "***************",  # Replace with your OpenWeatherMap API key
}

# Make API request and get response
response = requests.get(api_endpoint, params=api_params)
data = response.json()

# Extract relevant data
#this can be edited out based on requirements. print(data) before editing
weather_data = {
    "city": data["name"],
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "wind_speed": data["wind"]["speed"]
}

# Extract values from the dictionary
#this could be printed out, asigned to new variable, or use in other functions
city = weather_data['city']
temperature = weather_data['temperature']
humidity = weather_data['humidity']
wind_speed = weather_data['wind_speed']

# Convert to a pandas DataFrame
weather_df = pd.DataFrame([weather_data])

# Add a timestamp column
weather_df['time'] = datetime.now()

# Create a function to convert Kelvin temperature to Celsius
def kelvin_to_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius.

    Parameters:
    - kelvin (float): Temperature in Kelvin.

    Returns:
    - float: Temperature in Celsius.
    """
    celsius = kelvin - 273.15
    return round(celsius, 2)

weather_df['temperature_celsius'] = weather_df['temperature'].apply(kelvin_to_celsius)

# View DataFrame
print(weather_df)
