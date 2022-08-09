from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://facebook.com")

driver.implicitly_wait(10)
images = driver.find_elements(By.TAG_NAME, 'img')

for img in images:
    
    imgsource = img.get_attribute('src')
    r = requests.get(imgsource)
    print(imgsource)
    print(r.headers['Content-length'])

    