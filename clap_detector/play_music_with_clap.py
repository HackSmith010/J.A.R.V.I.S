import random
import pygame
from pygame import mixer
import time

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from clap_detector.clap_detector import *

def play_music(folder_path):
    # This print is user-facing and good to keep
    print(f"🎶 Now playing a random song...") 
    
    music_files = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]
    
    if not music_files:
        print("No .mp3 files found in the folder.")
        return
    
    selected_file = random.choice(music_files)
    music_path = os.path.join(folder_path, selected_file)
    
    try:
        pygame.init()
        mixer.init(frequency=44100, size=-16, channels=2, buffer=2048)
        
        mixer.music.load(music_path)
        mixer.music.play()
        
        time.sleep(0.1) 
        
        while mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
        print("Finished playing.")
        
    except Exception as e:
        print(f"An error occurred while playing music: {e}")
    finally:
        mixer.music.stop()
        mixer.quit()
        pygame.quit()


if __name__ == "__main__":
    MUSIC_FOLDER = "/home/hacksmith010/Programming/Personal/Jarvis/Music" 
    print("Application started. Waiting for clap trigger...")
    
    if clap_detect():
        print("Trigger received. Starting music player...")
        if not os.path.isdir(MUSIC_FOLDER):
            print(f"Error: Music folder not found at '{MUSIC_FOLDER}'")
        else:
            play_music(MUSIC_FOLDER)
    else:
        print("Application exiting.")
    
