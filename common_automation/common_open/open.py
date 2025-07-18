import pyautogui as ui
import time
import random

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from jarvis_speak.speak import speak
from jarvis_dlg_dataset.dlg import *    

def open(query):
    x = random.choice(open_dld)
    speak(x + query)
    time.sleep(0.5)
    ui.hotkey("win")
    time.sleep(0.2)
    ui.write(query)
    time.sleep(0.5)
    ui.press("enter")
    