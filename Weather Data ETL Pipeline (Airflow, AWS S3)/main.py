import json
from datetime import datetime
import pandas as pd
import requests

city_name = "Auckland"
base_url = "https://api.openweathermap.org/data/2.5/weather?q="

with open("api_key.txt", 'r') as f:
    api_key = f.read()

full_url = base_url + city_name + "&appid=" + api_key

def etl_weather_data(url):
    # Extract: make HTTP GET request to OpenWeatherMap API
    r = requests.get(url)
    data = r.json()

    # Transform: create a simplified dictionary with relevant fields
    transformed_data = {
        'City': data['name'],
        'Description': data['weather'][0]['description'],
        'Temperature (C)': round(data['main']['temp'] - 273.15,1),
        'Feels Like (C)': round(data['main']['feels_like'] - 273.15,1),
        'Minimum Temperature (C)': round(data['main']['temp_min'] - 273.15,1),
        'Maximum Temperature (C)': round(data['main']['temp_max'] - 273.15,1),
        'Pressure': data['main']['pressure'],
        'Humidity': data['main']['humidity'],
        'Wind Speed': data['wind']['speed'],
        'Time of Record': datetime.fromtimestamp(data['dt'] + data['timezone']),
        'Sunrise (local time)': datetime.fromtimestamp(data['sys']['sunrise'] + data['timezone']),
        'Sunset (local time)': datetime.fromtimestamp(data['sys']['sunset'] + data['timezone'])
    }
    # wrap dictionary in a list to make it compatible with pandas DataFrame
    df_data = pd.DataFrame([transformed_data])
    
    # Load: save the transformed data to a CSV file
    df_data.to_csv('weather_data_auckland.csv', index=False)

if __name__ == "__main__":
    etl_weather_data(full_url)