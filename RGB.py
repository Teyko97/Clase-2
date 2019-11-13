from pyfirmata import Arduino
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
    

