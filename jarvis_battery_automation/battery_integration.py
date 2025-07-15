import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from jarvis_battery_automation.battery_alert import *
from jarvis_battery_automation.battery_plug_check import *
from check_battery_percent import *

def battery_cmd(query):
    if "check battery percentage" in query or "battery percentage" in query:
        battery_percentage()