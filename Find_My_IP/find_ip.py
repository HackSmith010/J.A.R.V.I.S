import requests
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def find_my_ip():
    response = requests.get('https://api64.ipify.org?format=json')
    return response.json()['ip']