import psutil
import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from jarvis_speak.speak import speak
from jarvis_dlg_dataset.dlg import plug_in, plug_out

def check_plugin_status():
    battery = psutil.sensors_battery()
    previous_status = battery.power_plugged
    
    while True:
        battery = psutil.sensors_battery()
        
        if battery.power_plugged != previous_status:
            if battery.power_plugged:
                random_low = random.choice(plug_in)
                speak(random_low)
            else:
                random_low = random.choice(plug_out)
                speak(random_low)
                
            previous_status = battery.power_plugged