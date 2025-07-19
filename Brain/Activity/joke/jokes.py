import requests

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def get_random_jokes():
    headers = {
        'Accept': 'application/json',
    }
    res = requests.get('https://icanhazdadjoke.com/', headers=headers)
    return res.json()['joke']