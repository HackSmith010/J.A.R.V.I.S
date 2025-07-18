import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import pywhatkit
import random

from jarvis_dlg_dataset.dlg import *
from jarvis_speak.speak import speak

def search_google(query):
    dlg = random.choice(search_result)
    pywhatkit.search(query)
    speak(dlg)
    