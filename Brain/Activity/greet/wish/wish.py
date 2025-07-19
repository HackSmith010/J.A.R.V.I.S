import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from datetime import date,datetime
import random

from jarvis_speak.speak import speak
from jarvis_dlg_dataset.dlg import *

today = date.today()
formatted_date = today.strftime("%d %b %y")
nowx = datetime.now()

def wish():
    current_hour = nowx.hour
    if 5 <= current_hour < 12:
        gm_dlg = random.choice(good_morningdlg)
        speak(gm_dlg)
        
    elif 12 <= current_hour < 16:
        ga_dlg = random.choice(good_afternoondlg)
        speak(ga_dlg)
        
    elif 16 <= current_hour < 21:
        ge_dlg = random.choice(good_eveningdlg)
        speak(ge_dlg)
        
    else:
        gn_dlg = random.choice(good_nightdlg)
        speak(gn_dlg)