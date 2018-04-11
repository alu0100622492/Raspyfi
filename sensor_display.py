# Example for using the Grove I2C color LCD
import grove_rgb_lcd
from grove_rgb_lcd import *

while(True):
    setText("Hello desde la pantalla\nLCD ")
    setRGB(0,128,64)
    for c in range(0,255):
        setRGB(c,255-c,0)
        time.sleep(0.01)
    setRGB(0,255,0)
    setText("Adios, mi ninio")
    time.sleep(1.5)
