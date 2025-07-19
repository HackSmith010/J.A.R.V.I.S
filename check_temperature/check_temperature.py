from dotenv import load_dotenv
import requests
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from jarvis_speak.speak import speak
from jarvis_listen.listen import listen

load_dotenv()

def check_temperature(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        
        if 'main' in data:
            temperature = data['main']['temp']
            return temperature
        else:
            print("Error: 'main' key not found in the API response.")
            return None
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        return None
    
def Temp():
    city = "Mumbai"
    
    temperature = check_temperature(city)
    
    if temperature is not None:
        speak(f"The temperature in {city} is {temperature} degrees Celsius,Sir.")
    else:
        speak("Temperature data is not available.")