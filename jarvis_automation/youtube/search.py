import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import webbrowser
import pyautogui as ui
import random
import time
from jarvis_speak.speak import speak
from jarvis_dlg_dataset.dlg import *

def youtube_search(text):
    dlg = random.choice(yt_search)
    speak(dlg)
    webbrowser.open("https://www.youtube.com/")
    time.sleep(2)
    ui.press("/")
    ui.write(text)
    s12 = random.choice(s1)
    speak(s12)
    time.sleep(0.5)
    ui.press("enter")
    s12 = random.choice(s2)
    speak(s12)
    
youtube_search("tech with tim")