#import grovepi
#import math
## Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
## This example uses the blue colored sensor.
## SIG,NC,VCC,GND
#sensor = 4  # The Sensor goes on digital port 4.

## temp_humidity_sensor_type
## Grove Base Kit comes with the blue sensor.
#blue = 0    # The Blue colored sensor.
#white = 1   # The White colored sensor.

#while True:
    #try:
        ## This example uses the blue colored sensor. 
        ## The first parameter is the port, the second parameter is the type of sensor.
        #[temp,humidity] = grovepi.dht(sensor,blue)  
        #if math.isnan(temp) == False and math.isnan(humidity) == False:
            #print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))

    #except IOError:
        #print ("Error")


        
        
import time,sys
import RPi.GPIO as GPIO
import smbus

debug = 0
# use the bus that matches your raspi version
rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = smbus.SMBus(1)
else:
    bus = smbus.SMBus(0)

class th02:
	
	ADDRESS = 0x40

	TH02_REG_STATUS = 0x00
	TH02_REG_DATA_H = 0x01
	TH02_REG_DATA_L = 0x02
	TH02_REG_CONFIG = 0x03
	TH02_REG_ID = 0x11

	TH02_STATUS_RDY_MASK = 0x01

	TH02_CMD_MEASURE_HUMI = [0x01]
	TH02_CMD_MEASURE_TEMP = [0x11]

	SUCCESS = 0
	
	def getTemperature(self):
		bus.write_i2c_block_data(self.ADDRESS, self.TH02_REG_CONFIG, self.TH02_CMD_MEASURE_TEMP)
		
		while 1:
			status=self.getStatus()
			if debug:
				print("st:",status)
			if status:
				break
		t_raw=bus.read_i2c_block_data(self.ADDRESS, self.TH02_REG_DATA_H,3)
		if debug:
			print(t_raw)
		temperature = (t_raw[1]<<8|t_raw[2])>>2
		return (temperature/32.0)-50.0
		
	def getHumidity(self):
		bus.write_i2c_block_data(self.ADDRESS, self.TH02_REG_CONFIG, self.TH02_CMD_MEASURE_HUMI)
		
		while 1:
			status=self.getStatus()
			if debug:
				print("st:",status)
			if status:
				break
		t_raw=bus.read_i2c_block_data(self.ADDRESS, self.TH02_REG_DATA_H,3)
		if debug:
			print(t_raw)
		temperature = (t_raw[1]<<8|t_raw[2])>>4
		return (temperature/16.0)-24.0
		
	def getStatus(self):
		status=bus.read_i2c_block_data(self.ADDRESS, self.TH02_REG_STATUS,1)
		if debug:
			print(status)
		if status[0] & self.TH02_STATUS_RDY_MASK != 1:
			return 1
		else:
			return 0

if __name__ == "__main__":		
	t= th02()
	while True:
		print(t.getTemperature(),t.getHumidity())
		time.sleep(.5)
