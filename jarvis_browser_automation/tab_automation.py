import pyautogui as ui
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def new_tab(): 
    ui.hotkey("ctrl", "t")
    
def new_window(): 
    ui.hotkey("ctrl", "n")
    
def close_tab(): 
    ui.hotkey("ctrl", "w")
    
def browser_menu(): 
    ui.hotkey("ctrl", "f")
    
def zoom_in(): 
    ui.hotkey("ctrl", "+")
    
def zoom_out(): 
    ui.hotkey("ctrl", "-")
    
def refresh_page(): 
    ui.hotkey("ctrl", "r")
    
def next_tab(): 
    ui.hotkey("ctrl", "tab")
    
def prev_tab(): 
    ui.hotkey("ctrl", "shift", "tab")
    
def open_history(): 
    ui.hotkey("ctrl", "h")
    
def open_bookmarks(): 
    ui.hotkey("ctrl", "b")
    
def go_back(): 
    ui.hotkey("alt", "left")
    
def go_forward(): 
    ui.hotkey("alt", "right")
    
def open_dev_tools(): 
    ui.hotkey("ctrl", "shift", "i")
    
def private_tab(): 
    ui.hotkey("ctrl", "shift", "p")
    
def full_screen(): 
    ui.hotkey("f11")
    
def open_downloads(): 
    ui.hotkey("ctrl", "shift", "y")
