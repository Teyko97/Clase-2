from pyfirmata import Arduino
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium .webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#creamos un objeto de la clase arduino
board = Arduino ("COM6")
#rojo
led1 = board.get_pin('d:11:o')
#verde
led2 = board.get_pin('d:10:o')
#azul
led3 = board.get_pin('d:9:o')

class color:
    def __init__(self,color):
        self.color = color

color = input("Ingrese el color que desea: ")
        
if(color == "verde"):
    led2.write(1)
    led1.write(0)
    led3.write(0)
if(color == "rojo"):
    led2.write(0)
    led1.write(1)
    led3.write(0)   
if(color == "azul"):
    led2.write(0)
    led1.write(0)
    led3.write(1)
if(color == "morado"):
    led2.write(0)
    led1.write(1)
    led3.write(1)
if(color == "naranja"):
    led2.write(1)
    led1.write(1)
    led3.write(0)

driver = webdriver.Chrome(ChromeDriverManager().install())
phone = "6621673519" 
driver.get('https://api.whatsapp.com/send?phone=521'+ phone + '&text=&source=&data=')
driver.find_element_by_id('action-button').click()
time.sleep(5)
driver.find_element_by_link_text('usar WhatsApp Web').click()
print("por favor registre su codigo QR")
time.sleep(30)
driver.find_element_by_class_name('_3u328').send_keys(color)
time.sleep(10)
driver.find_element_by_class_name('_3M-N-').click()
