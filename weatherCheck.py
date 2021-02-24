import configparser
import requests
import sys


def weatherCity(city):

    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=526272e4ba362effe418d51c6b2139cc&q='
    url = api_address + city
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    # print(json_data)
    # print(formatted_data)

    return formatted_data