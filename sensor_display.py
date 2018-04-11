#!/usr/bin/python
# -*- coding: utf-8 -*- 

import grove_rgb_lcd
from grove_rgb_lcd import *
import grovepi

# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# SIG,NC,VCC,GND
sensor = 4

while True:
    try:
        [temp,humidity] = grovepi.dht(sensor,1)
        print temp, humidity
        
        time.sleep(1)
        setRGB(0,128,64)
        setText("La temp = %.02f C humedad =%.02f%%"%(temp, humidity))
        #setEditorData("Hola",temp.data().toString())
        setRGB(0,128,64)
        for c in range(0,255):
            setRGB(c,255-c,0)
            time.sleep(0.01)
        setRGB(255,0,0)
        setText("¡¡¡INFORMACION!!!")
        setRGB(0,255,0)
        time.sleep(1.5)

    except IOError:
        print "Error"
        


#while(True):
    #setText("Hello desde la pantalla\nLCD ")
    #setRGB(0,128,64)
    #for c in range(0,255):
        #setRGB(c,255-c,0)
        #time.sleep(0.01)
    #setRGB(0,255,0)
    #setText("Adios, mi ninio")
    #time.sleep(1.5)
