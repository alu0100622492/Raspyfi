#import sensor_temperatura
#import time
#from sensor_acelerometro import ADXL345
#from config_firebase import db

#ADXL345_DEVICE = 0x53
#p = ADXL345(ADXL345_DEVICE)
#while True:
        #axes = p.getAxes(True)
        #print "ADXL345 on address 0x%x:" % (p.address)
        #print "   x = %.3fG" % ( axes['x'] )
        #print "   y = %.3fG" % ( axes['y'] )
        #print "   z = %.3fG" % ( axes['z'] )
        #if(db.child('/sensores').child('/acelerometro').child('x').get()==axes['x'] or db.child('/sensores').child('/acelerometro').child('y').get()==axes['y'] or db.child('/sensores').child('/acelerometro').child('z').get()==axes['z']):
                #print("No hay actualizacion de valores")
        #else:
            #db.child('/sensores').child('/acelerometro').update({'x':axes['x']})
            #db.child('/sensores').child('/acelerometro').update({'y':axes['y']})
            #db.child('/sensores').child('/acelerometro').update({'z':axes['z']})
            
        
        #time.sleep(2)##cambiar a 0.5
