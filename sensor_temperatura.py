#import grovepi

## Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
## SIG,NC,VCC,GND
#sensor = 4

#while True:
    #try:
        #[temp,humidity] = grovepi.dht(sensor,1)
        #print "temp =", temp, " humidity =", humidity

    #except IOError:
        #print "Error"


#!/usr/bin/env python
#
# GrovePi Example for using the Grove Temperature Sensor (http://www.seeedstudio.com/wiki/Grove_-_Temperature_Sensor)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#
'''
## License
The MIT License (MIT)
GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
# NOTE: 
# 	The sensor uses a thermistor to detect ambient temperature.
# 	The resistance of a thermistor will increase when the ambient temperature decreases.
#	
# 	There are 3 revisions 1.0, 1.1 and 1.2, each using a different model thermistor.
# 	Each thermistor datasheet specifies a unique Nominal B-Constant which is used in the calculation forumla.
#	
# 	The second argument in the grovepi.temp() method defines which board version you have connected.
# 	Defaults to '1.0'. eg.
# 		temp = grovepi.temp(sensor)        # B value = 3975
# 		temp = grovepi.temp(sensor,'1.1')  # B value = 4250
# 		temp = grovepi.temp(sensor,'1.2')  # B value = 4250

#import time
#import grovepi

## Connect the Grove Temperature Sensor to analog port A0
## SIG,NC,VCC,GND
#sensor = 0

#while True:
    #try:
        #temp = grovepi.temp(sensor,'1.1')
        #print("temp =", temp)
        #time.sleep(.5)

    #except KeyboardInterrupt:
        #break
    #except IOError:
        #print ("Error")
        
        
        
        
        
        
import grovepi
import math
from config_firebase import db

#-------------------------------------------------------------------------


# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
sensor = 3  # The Sensor goes on digital port 4.

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

while True:
    try:
        # This example uses the blue colored sensor. 
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = grovepi.dht(sensor,blue)  
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
            if(db.child('/sensores').child('/termometro').child('temperatura').get()==temp or db.child('/sensores').child('/termometro').child('humedad').get()==humidity):
                print("No hay actualizacion de valores")
            else:
                db.child('/sensores').child('/termometro').update({'temperatura':temp})
                db.child('/sensores').child('/termometro').update({'humedad':humidity})
            
    except IOError:
        print ("Error")


##import grovepi
#import grovepi
## Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
## SIG,NC,VCC,GND
#sensor = 4

#while True:
    #try:
        #[temp,humidity] = grovepi.dht(sensor,1)
        #print "temp =", temp, " humidity =", humidity

    #except IOError:
        #print "Error"

