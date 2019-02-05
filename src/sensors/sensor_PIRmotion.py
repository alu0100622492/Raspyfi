#import time
#import grovepi

## Connect the Grove PIR Motion Sensor to digital port D8
## SIG,NC,VCC,GND
#pir_sensor = 8

#grovepi.pinMode(pir_sensor,"INPUT")

#while True:
    #try:
        ## Sense motion, usually human, within the target range
        #if grovepi.digitalRead(pir_sensor):
            #print 'Motion Detected'
        #else:
            #print '-'

        ## if your hold time is less than this, you might not see as many detections
        #time.sleep(.2)

    #except IOError:
        #print "Error"
        
        
import time
import grovepi
from config_firebase import db
# Connect the Grove PIR Motion Sensor to digital port D8
# SIG,NC,VCC,GND
pir_sensor = 8

grovepi.pinMode(pir_sensor,"INPUT")

while True:
    try:
        # Sense motion, usually human, within the target range
        ## senial 1 si deteta senial 0 sino
        if(grovepi.digitalRead(pir_sensor) == db.child('/sensores').child('/antirobo').child('valor').get()):
                print("No hay actualizacion de valores")
        else:
            
            if grovepi.digitalRead(pir_sensor):
                db.child('/sensores').child('/antirobo').update({'valor':grovepi.digitalRead(pir_sensor)})
                print 'Detectado Movimiento'
            else:
                db.child('/sensores').child('/antirobo').update({'valor':grovepi.digitalRead(pir_sensor)})
                print 'zZz'

        # if your hold time is less than this, you might not see as many detections
        time.sleep(.2)

    except IOError:
        print "Error"
