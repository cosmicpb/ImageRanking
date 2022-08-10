from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import click
import time

class obj:
    def __init__(self, url, size):
        self.url = url
        self.size = size


@click.command()
@click.option('-h', required=True, type=str)
@click.option('-t', required=True, type=str)


def func(h, t):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(h)
    time.sleep(int(t))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    images = driver.find_elements(By.TAG_NAME, 'img')
    objs = []
    for img in images:
        
        imgsource = img.get_attribute('src')
        if(imgsource):
            r = requests.get(imgsource)
            #print(imgsource)
            el = r.headers.get('Content-length')
            if(el.isdigit()):

                el = int(el)/1024
                fel = "{:.2f}".format(el)

                if(obj(imgsource, float(fel)) not in objs):
                    objs.append(obj(imgsource,float(fel)))                
                
                #print("Image Size: %.2f kB" % el)
            #else:
                #print('There is no Content-Length in .head')

    objs.sort(key=lambda x: x.size)
    for ent in objs:
        print(getattr(ent, 'url'))
        print(getattr(ent, 'size'))
        
       
        



if __name__ == '__main__':
    
    func()