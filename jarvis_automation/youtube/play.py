import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import time
import pywhatkit as kt
import random
import pyautogui as ui
from jarvis_speak.speak import speak
from jarvis_dlg_dataset.dlg import *

def play_on_youtube(text):
    playdlg = random.choice(playsong)
    speak(playdlg)
    kt.playonyt(text)
    time.sleep(3)
    speak(random.choice(plays) + text)
    ui.press("space")
    
play_on_youtube("ram siya ram")
