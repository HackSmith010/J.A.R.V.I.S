import pyautogui as ui
import random
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from jarvis_dlg_dataset.dlg import s1,s2
from jarvis_speak.speak import speak

def search_manual(query):
    ui.press("/")  
    ui.write(query)
    s12 = speak(random.choice(s1))
    speak(s12)
    time.sleep(0.5)
    ui.press("enter")
    s12 = speak(random.choice(s2))
    speak(s12)
    
time.sleep(2)
# search_manual("Tech with Tim")