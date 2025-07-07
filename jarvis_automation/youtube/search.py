import sys
import os
import time
import random
import pyautogui as ui
import webbrowser
import subprocess

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from jarvis_speak.speak import speak
from jarvis_dlg_dataset.dlg import yt_search, s1, s2

def focus_browser():
    try:
        time.sleep(3)
        subprocess.run(['wmctrl', '-a', 'YouTube'], check=True)
    except subprocess.CalledProcessError:
        print("[❌] Could not focus the browser window")

def youtube_search(query):
    speak(random.choice(yt_search))

    webbrowser.open("https://www.youtube.com")
    focus_browser()

    time.sleep(2)
    ui.press("/")  
    ui.write(query)
    speak(random.choice(s1))
    time.sleep(0.5)
    ui.press("enter")
    time.sleep(2)
    speak(random.choice(s2))

# if __name__ == "__main__":
#     youtube_search("thala for a resean... its bday today")
