import time 
import psutil
import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from jarvis_speak.speak import speak
from jarvis_dlg_dataset.dlg import *

def battery_alert():
    while True:
        time.sleep(10)
        battery = psutil.sensors_battery()
        percent = int(battery.percent)
        
        if percent < 20:
            random_low =  random.choice(low_b)
            speak(random_low)
        elif percent < 10:
            random_low = random.choice(low_b)
            speak(random_low)
            
        elif percent < 80:
            random_full = random.choice(full_battery)
            speak(random_full)
        else:
            pass
        
        time.sleep(1500)
        
def battery_alert1():
    time.sleep(10)
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    
    if percent < 20:
        random_low =  random.choice(low_b)
        speak(random_low)
    elif percent < 10:
        random_low = random.choice(low_b)
        speak(random_low)
        
    elif percent < 80:
        random_full = random.choice(full_battery)
        speak(random_full)
    else:
        speak("Sir, your device is in perfect battery level")
    
    time.sleep(1500)