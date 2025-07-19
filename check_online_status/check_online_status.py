import requests

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def is_online(url="https://google.com",timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code >= 200 and response.status_code < 300
    except requests.ConnectionError:
        return False
    
def internet_status():
    if is_online():
        return "Online"
    else:
        return "Offline"    