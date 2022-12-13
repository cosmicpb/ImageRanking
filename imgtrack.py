from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
from tqdm import tqdm
from alive_progress import alive_bar
import validators
import requests
import click
import time
import gui

class obj:
    def __init__(self, url, size, time):
        self.url = url
        self.size = size
        self.time = time


@click.command()
@click.option('-u', required=True, type=str)
@click.option('-t', required=True, type=str)
@click.option('-h', type=bool, default=False)

def func(u, t, h):

    ##Selenium Options
    options = Options()
    if h:
        options.add_argument('--headless') 
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    ##ChromeDriver install
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    ##Show apresentation
    gui.hellogui(u, t)


    ##Enter the page, wait loading the entire page and scroll down to the bottom page
    driver.get(u)
    time.sleep(3)

    
    height = driver.execute_script("return document.body.scrollHeight")
    interval = height/int(t)
    
    y = 100
    for i in tqdm(range(int(t))):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, "+str(y)+");")
        y = y + interval
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    ##time.sleep(int(t))
    

    ##Find images
    images = driver.find_elements(By.TAG_NAME, 'img')
    
    gui.div()
    print('Images found: ' + str(len(images)))

    gui.div()
    ##Declaring WebElements Array and webelements size sum
    objs = []
    imgsum = 0
    print('Sizing images:')
    
    ##iterating in images
    for img in tqdm(images):
        
        ##Taking the tag source
        imgsource = img.get_attribute('src')
        imgsource = str(imgsource)
        if(validators.url(imgsource)):
            now = datetime.now()
            tmnow = now.strftime("%d_%m_%Y.%H_%M_%S")
            r = requests.get(imgsource)

            'Content-Lenght'                    

            el = len(r.content)/1024
            fel = "{:.2f}".format(el)
            
            imgsum = imgsum + el
            if(obj(imgsource, float(fel), tmnow) not in objs):
                objs.append(obj(imgsource,float(fel), tmnow))  

            
                


    objs.sort(key=lambda x: x.size)



    for ent in objs:
        print(str(getattr(ent, 'time')))
        print(getattr(ent, 'url'))
        print(str(getattr(ent, 'size')) + ' kB')
    imgsum_f = "{:.2f}".format(imgsum)
    print('Tamanho total das imagens na página: ' + str(imgsum_f) + ' kB')
        
       
        
if __name__ == '__main__':
    
    func()