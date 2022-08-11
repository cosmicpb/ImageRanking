from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
import requests
import click
import time

class obj:
    def __init__(self, url, size, time):
        self.url = url
        self.size = size
        self.time = time


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
    time.sleep(int(t))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    images = driver.find_elements(By.TAG_NAME, 'img')
    objs = []
    imgsum = 0
    for img in images:
        
        imgsource = img.get_attribute('src')
        if(imgsource):

            r = requests.get(imgsource)
            #print(imgsource)
            el = str(r.headers.get('Content-length'))
            if(el.isdigit()):

                el = int(el)/1024
                fel = "{:.2f}".format(el)
                now = datetime.now()
                tmnow = now.strftime("%d_%m_%Y.%H_%M_%S")
                imgsum = imgsum + el
                if(obj(imgsource, float(fel), tmnow) not in objs):
                    objs.append(obj(imgsource,float(fel), tmnow))                
                
                #print("Image Size: %.2f kB" % el)
            #else:
                #print('There is no Content-Length in .head')

    objs.sort(key=lambda x: x.size)
    for ent in objs:
        print(str(getattr(ent, 'time')))
        print(getattr(ent, 'url'))
        print(str(getattr(ent, 'size')) + ' kB')
    imgsum_f = "{:.2f}".format(imgsum)
    print('Tamanho total das imagens na página: ' + str(imgsum_f) + ' kB')
        
       
        
if __name__ == '__main__':
    
    func()