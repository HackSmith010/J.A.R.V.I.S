import random
import sys
import os
import pyautogui as ui
import time
import webbrowser
import difflib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from jarvis_dlg_dataset.dlg import *
from jarvis_speak.speak import speak

def openWeb(query):
    website_name = query.strip().lower()
    
    if website_name in websites:
        random_dlg = random.choice(open_dld)
        speak(random_dlg + query)
        url = websites[website_name]
        webbrowser.open(url)
        randomsuccess = random.choice(success_open)
        speak(randomsuccess)
    else:
        matches = difflib.get_close_matches(website_name, websites.keys())
        if matches:
            random_dlg = random.choice(open_dld)
            randomopen2 = random.choice(open_maybe)
            closet_match = matches[0]
            speak(randomopen2 + random_dlg + query)
            url = websites[closet_match]
            webbrowser.open(url)
            randomsuccess = random.choice(success_open)
            speak(randomsuccess)
        else:
            random_sorry = random.choice(sorry_open)
            speak(random_sorry + " named " + query)
            
            
      