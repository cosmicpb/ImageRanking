from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://avon.mx")

driver.implicitly_wait(10)
images = driver.find_elements(By.TAG_NAME, 'img')

for img in images:
    print(img.accessible_name)
    print(img.get_attribute('src'))

    