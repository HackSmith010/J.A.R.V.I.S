import pyautogui as ui
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def toggle_captions(self):
        ui.press("c")
        
def increase_font_size(self):
    ui.press("+")
    
def decrease_font_size(self):
    ui.press("-")
    
def rotate_text_opacity(self):
    ui.press("o")
    
def rotate_window_opacity(self):
    ui.press("w")
