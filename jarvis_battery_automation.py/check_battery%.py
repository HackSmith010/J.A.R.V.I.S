import psutil
import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from jarvis_speak.speak import speak

def battery_percentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    speak(f"The device is running on {percent}% battery power.")