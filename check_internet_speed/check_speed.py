import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from jarvis_speak.speak import speak

def get_internet_speed():
    try:
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_service = Service()
        driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

        driver.get("https://fast.com/")
        speak("Checking internet speed...")
        time.sleep(11)
        
        WebDriverWait(driver , timeout=60).until(
            EC.presence_of_element_located((By.ID, "speed-value"))
        )
        
        speed_element = driver.find_element(By.ID, "speed-value")
        speed_value = speed_element.text

        driver.quit()
        return speed_value
    except Exception as e:
        driver.quit()
        return f"Error: {e}"
    finally:
        driver.quit()
        
def check_internet_speed():
    speed_result = get_internet_speed()
    
    if speed_result is not None:
        speak(f"Sir , your internet speed is : {speed_result} Mbps")
    else:
        speak("Error occurred while checking internet speed.")
        
check_internet_speed()