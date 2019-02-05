
        
## GrovePi + Grove Ultrasonic Ranger

#from grovepi import *

## Connect the Grove Ultrasonic Ranger to digital port D4
## SIG,NC,VCC,GND

#ultrasonic_ranger = 4

#while True:
    #try:
        ## Read distance value from Ultrasonic
        #print ultrasonicRead(ultrasonic_ranger)

    #except TypeError:
        #print "Error"
    #except IOError:
        #print "Error"
        
## GrovePi + Grove Ultrasonic Ranger

import grovepi

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

ultrasonic_ranger = 4

while True:
    try:
        # Read distance value from Ultrasonic
        print grovepi.ultrasonicRead(ultrasonic_ranger)

    except TypeError:
        print "Error type"
    except IOError:
        print "Error io"
############################################3

#import grovepi

## Connect the Grove Ultrasonic Ranger to digital port D4
## SIG,NC,VCC,GND
#ultrasonic_ranger = 4

#while True:
    #try:
        ## Read distance value from Ultrasonic
        #print(grovepi.ultrasonicRead(ultrasonic_ranger))

    #except TypeError:
        #print ("Error")
    #except IOError:
        #print ("Error")


#######################################3

##!/usr/bin/python
##+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
##|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
##+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
##
## ultrasonic_2.py
## Measure distance using an ultrasonic module
## in a loop.
##
## Author : Matt Hawkins
## Date   : 28/01/2013

## -----------------------
## Import required Python libraries
## -----------------------
#import time
#import RPi.GPIO as GPIO

## -----------------------
## Define some functions
## -----------------------

#def measure():
  ## This function measures a distance
  #GPIO.output(GPIO_TRIGGER, True)
  #time.sleep(0.00001)
  #GPIO.output(GPIO_TRIGGER, False)
  #start = time.time()

  #while GPIO.input(GPIO_ECHO)==0:
    #start = time.time()

  #while GPIO.input(GPIO_ECHO)==1:
    #stop = time.time()

  #elapsed = stop-start
  #distance = (elapsed * 34300)/2

  #return distance

#def measure_average():
  ## This function takes 3 measurements and
  ## returns the average.
  #distance1=measure()
  #print "Distancia 1", distance1
  #time.sleep(0.1)
  #distance2=measure()
  #time.sleep(0.1)
  #distance3=measure()
  #distance = distance1 + distance2 + distance3
  #distance = distance / 3
  #print "distancia",distance
  #return distance

## -----------------------
## Main Script
## -----------------------

## Use BCM GPIO references
## instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)

## Define GPIO to use on Pi
#GPIO_TRIGGER = 23
#GPIO_ECHO    = 24

#print "Ultrasonic Measurement"

## Set pins as output and input
#GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
#GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

## Set trigger to False (Low)
#GPIO.output(GPIO_TRIGGER, False)

## Wrap main content in a try block so we can
## catch the user pressing CTRL-C and run the
## GPIO cleanup function. This will also prevent
## the user seeing lots of unnecessary error
## messages.
#try:

  #while True:
    #print "measure"
    #distance = measure_average()
    #print "Distance : %.1f" % distance
    #time.sleep(1)

#except KeyboardInterrupt:
  ## User pressed CTRL-C
  ## Reset GPIO settings
  #GPIO.cleanup()


####################################3

#import RPi.GPIO as GPIO
#import time

#TRIG = 23
#ECHO = 24

#print "Distancia en progreso"
#GPIO.setup(TRIG,GPIO.OUT)
#GPIO.setup(ECHO,GPIO.IN)

#GPIO.output(TRIG,False)
#print "Esperando por el sensor"
#time.sleep(2)

#GPIO.output(TRIG,True)
#time.sleep(0.00001)
#GPIO.output(TRIG,False)

#while GPIO.input(ECHO)==0:
    #pulse_start = time.time()

#while GPIO.input(ECHO)==1:
    #pulse_end = time.time()
    
#pulse_duration = pulse_end - pulse_start
#distance = pulse_duration * 17150
#distance = round(distance,2)

#print "Distancia:", distance,"cm"

#GPIO.cleanup()






