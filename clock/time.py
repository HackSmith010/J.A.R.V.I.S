import datetime

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from jarvis_speak.speak import speak

def time():
    try:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    except Exception as e:
        error_message = f"An error occured: {e}"
        print(error_message)
        speak(error_message)
        
def date():
    try:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        speak(f"Today's date is {current_date}")
    except Exception as e:
        error_message = f"An error occured: {e}"
        print(error_message)
        speak(error_message)
        