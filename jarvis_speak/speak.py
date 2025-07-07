import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

FIREFOX_BINARY_PATH = "/usr/lib/firefox/firefox"  

if not shutil.which(FIREFOX_BINARY_PATH):
    raise FileNotFoundError(f"Firefox binary not found at {FIREFOX_BINARY_PATH}")

firefox_options = Options()
firefox_options.binary_location = FIREFOX_BINARY_PATH
firefox_options.add_argument("--headless") 

firefox_service = Service()
driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

driver.get("https://tts.5e7en.me/")

def speak(text):
    try:
        text_box = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]'))
        )
        text_box.click()
        text_box.send_keys(text)
        print(f"[🗣️ Speaking]: {text}")

        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="button"]'))
        )
        button.click()

        time.sleep(min(0.2 + len(text) // 5, 5))

        text_box.clear()

    except Exception as e:
        print(f"[❌ Error in speak()]: {e}")
