import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import random
from jarvis_dlg_dataset.dlg import *
from jarvis_speak.speak import speak

def welcome():
    welcome = random.choice(welcomedlg)
    speak(welcome)