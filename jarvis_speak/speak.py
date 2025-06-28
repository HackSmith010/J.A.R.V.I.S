import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_service = Service()
driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

driver.get("https://tts.5e7en.me/")

def speak(text):
    element_to_click = WebDriverWait(driver,1).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="text"]'))
    )
    
    element_to_click.click()
    
    text_to_input = text
    element_to_click.send_keys(text_to_input)
    print(text_to_input)
    
    sleep_duration = min(0.2 + len(text) // 5,5)
    
    button_to_click = WebDriverWait(driver,1).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="button"]'))
    )
    
    button_to_click.click()
    
    time.sleep(sleep_duration)
    
    element_to_click.clear()
    
speak("hello")
