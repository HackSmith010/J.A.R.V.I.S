import pyautogui as ui
import random

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from jarvis_dlg_dataset.dlg import *
from jarvis_speak.speak import speak

def close():
    closedlg_random = random.choice(closedlg)
    speak(closedlg_random)
    ui.hotkey("alt", "f4")
    