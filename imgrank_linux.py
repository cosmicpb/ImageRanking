from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import click
import time

@click.command()
@click.option('-h', required=True, type=str)
@click.option('-t', required=True, type=str)

def func(h, t):

 
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get(h)
    time.sleep(t)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    images = driver.find_elements(By.TAG_NAME, 'img')
    
    for img in images:
        
        imgsource = img.get_attribute('src')
        if(imgsource):
            r = requests.get(imgsource)
            print(imgsource)
            el = r.headers.get('Content-length')
            if(el.isdigit()):
                
                el = int(el)/1024
                
                print("Image Size: %.2f kB" % el)
            else:
                print('There is no Content-Length in .head')


if __name__ == '__main__':
    
    func()