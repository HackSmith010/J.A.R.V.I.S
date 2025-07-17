import psutil
import random
import sys
import os
import asyncio

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from jarvis_speak.speak import speak
from jarvis_dlg_dataset.dlg import plug_in, plug_out

def check_plug_status():
    battery = psutil.sensors_battery()
    
    if battery is None:
        speak("Battery status not available.")
        return

    if battery.power_plugged:
        speak(random.choice(plug_in))
    else:
        speak(random.choice(plug_out))

