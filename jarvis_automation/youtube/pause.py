import pyautogui as ui
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def play():
    ui.press("space")
    
def pause():
    ui.press("space")