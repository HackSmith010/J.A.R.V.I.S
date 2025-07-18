import pyautogui as ui
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def scroll_up():
    ui.press("up")
    
def scroll_down():
    ui.press("down")

def scroll_to_top():
    ui.hotkey("home")
    
def scroll_to_bottom():
    ui.hotkey("end")
