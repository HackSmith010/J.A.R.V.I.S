import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import random
import time
from jarvis_speak.speak import speak
from jarvis_dlg_dataset.dlg import *
from jarvis_listen.listen import listen


import requests
def get_random_advice():
    response = requests.get("https://api.adviceslip.com/advice")
    data = response.json()
    advice = data["slip"]["advice"]
    return advice


def advice():
    while True:
        x = [ 600 , 550 , 580 , 400 , 3000 , 800 , 700 , 8200 , 8000 , 50 , 568 ]
        x = random.choice(x)
        time.sleep(x)
        speak("I have some advice for you , sir")
        query = listen().lower()
        if "yes tell me" in query or "tell me" in query or "yes" in query:
            advice = get_random_advice()
            speak(advice)
            pass
        else:
            speak("No problem sir , I am here to help you")
            pass
