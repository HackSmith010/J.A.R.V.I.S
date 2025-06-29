from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import shutil

FIREFOX_BINARY_PATH = "/usr/lib/firefox/firefox"  # Ensure this is correct

# Check if binary exists
if not shutil.which(FIREFOX_BINARY_PATH):
    raise FileNotFoundError(f"Firefox binary not found at {FIREFOX_BINARY_PATH}")

firefox_options = Options()
firefox_options.binary_location = FIREFOX_BINARY_PATH  # ✅ Correct way to set binary
# Comment out headless to see what's going on
# firefox_options.add_argument("--headless")

firefox_service = Service()
driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

driver.get("https://www.google.com")  # simple test
print("✅ Firefox launched and opened Google.")
