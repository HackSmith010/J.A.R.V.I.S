import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from jarvis_automation.youtube.others import *
from jarvis_automation.youtube.caption import *
from jarvis_automation.youtube.manual_search import *
from jarvis_automation.youtube.play import *
from jarvis_automation.youtube.pause import *
from jarvis_automation.youtube.search import *
from jarvis_automation.youtube.video_playback import *
from jarvis_dlg_dataset.dlg import *
from jarvis_listen.listen import listen
from jarvis_speak.speak import *

def youtube_cmd(query):
    query = query.strip().lower()
    
    if query in x :
        a = random.choice(q)
        speak(a)
        query = listen().lower()
        play_on_youtube(query)
        
    elif query in x1:
        pause()
        
    elif query in x2:
        play()
    
    elif query == "increase volume":
        volume_up()
    
    elif query == "decrease volume":
        volume_down()
    
    elif query == "seek forward":
        seek_forward()
    
    elif query == "seek backward":
        seek_backward()
        
    elif query == "seek forward 10s":
        seek_forward_10s()
    
    elif query == "seek backward 10s":
        seek_backward_10s()
        
    elif query == "seek to beginning":
        seek_start()
        
    elif query == "seek to end":
        seek_end()
        
    elif query == "play next video":
        next_video()
        
    elif query == "play previous video":
        previous_video()
        
    elif query == "increase playback speed":
        increase_playback_speed()
        
    elif query == "decrease playback speed":
        decrease_playback_speed()
        
    elif query == "turn on caption" or query == "turn off caption":
        toggle_captions()
    
    elif query == "increase font size":
        increase_font_size()
        
    elif query == "decrease font size":
        decrease_font_size()
        
    elif query == "rotate text opacity":
        rotate_text_opacity()
        
    elif query == "rotate window opacity":
        rotate_window_opacity()
        
    elif query == "mute" or query == "unmute":
        toggle_mute()
        
    elif query == "fullscreen":
        toggle_fullscreen()
        
    elif query == "turn on theatre mode" or query == "turn off theatre mode":
        toggle_theater_mode()
    
    elif query == "turn on miniplayer" or query == "turn off miniplayer":
        toggle_miniplayer()
        
    elif query == "exit fullscreen":
        exit_fullscreen()
        
    elif query == "focus on search box":
        focus_search_box()

youtube_cmd("carry minati")
