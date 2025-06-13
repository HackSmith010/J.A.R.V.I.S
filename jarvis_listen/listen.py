import speech_recognition as sr
import os
import threading
import time
from mtranslate import translate
from colorama import Fore, Style, init
from ctypes import *
from contextlib import contextmanager

init(autoreset=True)

# ALSA Warning Suppression
@contextmanager
def suppress_alsa_warnings():
    try:
        ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
        libc = CDLL('libasound.so.2')
        orig_error_handler = libc.__snd_lib_error_set_handler
        libc.__snd_lib_error_set_handler(ERROR_HANDLER_FUNC(lambda *args: None))
        yield
    finally:
        libc.__snd_lib_error_set_handler(orig_error_handler)

def print_loop():
    while True:
        try:
            print(Fore.LIGHTGREEN_EX + "I am Listening..." + " " * 50 + "\r", end="", flush=True)
        except:
            pass
        time.sleep(0.1)

def translate_hindi_to_english(txt):
    english_txt = translate(txt, to_language="en-us")
    return english_txt

def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 34000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.non_speaking_duration = 0.1
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        
        while True:
            try:
                audio = recognizer.listen(source, timeout=None)
                recognized_txt = recognizer.recognize_google(audio).lower()
                if recognized_txt:
                    translated_txt = translate_hindi_to_english(recognized_txt)
                    return translated_txt
                else:
                    return ""
            except sr.UnknownValueError:
                recognized_txt = ""
            except Exception as e:
                print(f"\nError: {str(e)}")
                return ""

def main():
    with suppress_alsa_warnings():
        print_thread = threading.Thread(target=print_loop, daemon=True)
        print_thread.start()
        
        while True:
            result = listen()
            if result:
                print(f"\nYou said: {result}")
                # Add your response handling here

if __name__ == "__main__":
    main()