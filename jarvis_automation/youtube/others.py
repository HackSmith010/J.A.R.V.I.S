import pyautogui as ui
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def toggle_mute(self):
    ui.press("m")
    
def toggle_fullscreen(self):
    ui.press("f")
    
def toggle_theater_mode(self):
    ui.press("t")
    
def toggle_miniplayer(self):
    ui.press("i")
    
def exit_fullscreen(self):
    ui.press("esc")
    
def focus_search_box(self):
    ui.press("/")
