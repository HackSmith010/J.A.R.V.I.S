import pyautogui as ui
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def play_pause(self):
    ui.press("space")
    
def volume_up(self):
    ui.press("up")
    
def volume_down(self):
    ui.press("down")
    
def seek_forward(self):
    ui.press("right")
    
def seek_backward(self):
    ui.press("left")
    
def seek_forward_10s(self):
    ui.press("l")
    
def seek_backward_10s(self):
    ui.press("j")
    
def seek_start(self):
    ui.press("home")
    
def seek_end(self):
    ui.press("end")
    
def seek_to_percent(self, percent):
    if 0 <= percent <= 90 and percent % 10 == 0:
        ui.press(str(percent // 10))
    
def next_video(self):
    ui.hotkey("shift", "n")
    
def previous_video(self):
    ui.hotkey("shift", "p")

def increase_playback_speed(self):
    ui.hotkey("shift", ".")
    
def decrease_playback_speed(self):
    ui.hotkey("shift", ",")