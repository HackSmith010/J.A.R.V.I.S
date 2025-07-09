import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def battery_cmd(query):
    if "check battery percentage" in query or "battery percentage" in query:
        check_battery