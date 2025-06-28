import os
import sys
import subprocess
import speech_recognition as sr
from colorama import Fore, init
import langdetect

init(autoreset=True)

sys.stderr = open(os.devnull, 'w')

def translate_transliterated_hindi(text, model="llama3.1"):
    prompt = f"""You are a translator. Translate only this transliterated Hindi to English and return only the translated sentence — no reasoning or explanation.

Hindi: {text}
English:"""

    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            text=True,
            capture_output=True,
            check=True
        )
        output = result.stdout.strip()
        lines = output.split("\n")
        for line in reversed(lines):
            if line.strip() and not line.lower().startswith("hindi:"):
                return line.strip().strip('"')
        return text  # fallback
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Translation Error: {e.stderr}")
        return text


def is_english(text):
    try:
        lang = langdetect.detect(text)
        return lang == "en"
    except:
        return False


def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 34000
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.1

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                print(Fore.LIGHTGREEN_EX + "\r🎤 I am Listening...", end="", flush=True)
                audio = recognizer.listen(source, timeout=None)

                print("\r" + " " * 80, end="")  # Clear line
                print(Fore.LIGHTYELLOW_EX + "\r🤖 Got it, Now Recognizing...", end="", flush=True)

                recognized_text = recognizer.recognize_google(audio).lower()

                if is_english(recognized_text):
                    print(Fore.BLUE + f"✅ You said: {recognized_text}")
                else:
                    translated = translate_transliterated_hindi(recognized_text)
                    print(Fore.BLUE + f"✅ You said: {translated}")

            except sr.UnknownValueError:
                print("\r" + " " * 80, end="")
                print(Fore.LIGHTRED_EX + "❌ Could not understand audio")
            except Exception as e:
                print(Fore.RED + f"⚠️ Error: {e}")
            finally:
                print("\r", end="", flush=True)


def hearing(model="llama3.1"):
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 34500
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.1

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=None)
            recognized_text = recognizer.recognize_google(audio).lower()

            if is_english(recognized_text):
                return recognized_text
            else:
                return translate_transliterated_hindi(recognized_text, model=model)

        except sr.UnknownValueError:
            return ""
        except Exception as e:
            print(Fore.RED + f"⚠️ Hearing Error: {e}")
            return ""

if __name__ == "__main__":
    print(Fore.CYAN + "🤖 Jarvis is now listening (press Ctrl+C to stop)...\n")
    listen()
