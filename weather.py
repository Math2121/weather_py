from dotenv import load_dotenv
from pprint import pprint
import os
import requests

load_dotenv()

def get_current_weather(city="Rio de Janeiro"):
    api_key = os.getenv('API_KEY')
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial'

    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    pprint(get_current_weather())