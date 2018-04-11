#import serial, time
#import smbus
#import math
#import RPi.GPIO as GPIO
#import struct
#import sys
 
#ser = serial.Serial('/dev/ttyAMA0',  9600, timeout = 0)   #Open the serial port at 9600 baud
#ser.flush()
 
#class GPS:
    ##The GPS module used is a Grove GPS module http://www.seeedstudio.com/depot/Grove-GPS-p-959.html
    #inp=[]
    ## Refer to SIM28 NMEA spec file https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/res/SIM28_DATA_File.zip
    #GGA=[]
 
    ##Read data from the GPS
    #def read(self):
        #while True:
            #GPS.inp=ser.readline()
            #if GPS.inp[:6] =='$GPGGA': # GGA data , packet 1, has all the data we need
                #break
            #time.sleep(0.1)
        #try:
            #ind=GPS.inp.index('$GPGGA',5,len(GPS.inp)) #Sometimes multiple GPS data packets come into the stream. Take the data only after the last '$GPGGA' is seen
            #GPS.inp=GPS.inp[ind:]
        #except ValueError:
            #print ""
        #GPS.GGA=GPS.inp.split(",")   #Split the stream into individual parts
        #return [GPS.GGA]
 
    ##Split the data into individual elements
    #def vals(self):
        #time=GPS.GGA[1]
        #lat=GPS.GGA[2]
        #lat_ns=GPS.GGA[3]
        #long=GPS.GGA[4]
        #long_ew=GPS.GGA[5]
        #fix=GPS.GGA[6]
        #sats=GPS.GGA[7]
        #alt=GPS.GGA[9]
        #return [time,fix,sats,alt,lat,lat_ns,long,long_ew]
 
#g=GPS()
#f=open("gps_data.csv",'w')   #Open file to log the data
##f=open("hola.csv",'w')   #Open file to log the data
#f.write("name,latitude,longitude\n")   #Write the header to the top of the file
#ind=0
#while True:
    #try:
        #x=g.read()  #Read from GPS
        #[t,fix,sats,alt,lat,lat_ns,long,long_ew]=g.vals() #Get the individial values
        #print "Time:",t,"Fix status:",fix,"Sats in view:",sats,"Altitude",alt,"Lat:",lat,lat_ns,"Long:",long,long_ew
        #s=str(t)+","+str(float(lat)/100)+","+str(float(long)/100)+"\n"   
        #f.write(s)   #Save to file
        #time.sleep(2)
    #except IndexError:
        #print "Unable to read"
    #except KeyboardInterrupt:
        #f.close()
        #print "Exiting"
        #sys.exit(0)
        
################################################################################################3
        
        
#import serial, time
#import smbus
#import math
#import RPi.GPIO as GPIO
#import struct
#import sys
 
#ser = serial.Serial('/dev/ttyAMA0',  9600, timeout = 0)	#Open the serial port at 9600 baud
#ser.flush()
 
#def readlineCR():
    #rv = ""
    #while True:
        #time.sleep(0.001)	# This is the critical part.  A small pause 
        					## works really well here.
        #ch = ser.read()        
        #rv += ch
        #if ch=='\r' or ch=='':
            #return rv
 
#class GPS:
	##The GPS module used is a Grove GPS module http://www.seeedstudio.com/depot/Grove-GPS-p-959.html
	#inp=[]
	## Refer to SIM28 NMEA spec file http://www.seeedstudio.com/wiki/images/a/a0/SIM28_DATA_File.zip
	#GGA=[]
 
	##Read data from the GPS
	#def read(self):	
		#while True:
			## GPS.inp=ser.readline()
			#GPS.inp = readlineCR().strip()
			#if GPS.inp[:6] =='$GPGGA': # GGA data , packet 1, has all the data we need
				#break
			#time.sleep(0.1)
		#try:
			#ind=GPS.inp.index('$GPGGA',5,len(GPS.inp))	#Sometimes multiple GPS data packets come into the stream. Take the data only after the last '$GPGGA' is seen
			#GPS.inp=GPS.inp[ind:]
		#except ValueError:
			#print ""
		#GPS.GGA=GPS.inp.split(",")	#Split the stream into individual parts
		#return [GPS.GGA]
 
	##Split the data into individual elements
	#def vals(self):
		#time=GPS.GGA[1]
		#lat=GPS.GGA[2]
		#lat_ns=GPS.GGA[3]
		#long=GPS.GGA[4]
		#long_ew=GPS.GGA[5]
		#fix=GPS.GGA[6]
		#sats=GPS.GGA[7]
		#alt=GPS.GGA[9]
		#return [time,fix,sats,alt,lat,lat_ns,long,long_ew]
 
#g=GPS()
#f=open("gps_data.csv",'w')	#Open file to log the data
#f.write("name,latitude,longitude\n")	#Write the header to the top of the file
#ind=0
#while True:
	#try:
		#x=g.read()	#Read from GPS
		#[t,fix,sats,alt,lat,lat_ns,long,long_ew]=g.vals()	#Get the individial values
		#print "Time:",t,"Fix status:",fix,"Sats in view:",sats,"Altitude",alt,"Lat:",lat,lat_ns,"Long:",long,long_ew
		#s=str(t)+","+str(float(lat)/100)+","+str(float(long)/100)+"\n"	
		#f.write(s)	#Save to file
		#time.sleep(2)
	#except IndexError:
		#print "Unable to read"
	#except KeyboardInterrupt:
		#f.close()
		#print "Exiting"
		#sys.exit(0)
	#except:
		#print "Raw String appears to be empty."

#########################################################################################
#import serial, time
#import smbus
#import math
#import RPi.GPIO as GPIO
#import struct
#import sys
#import ir_receiver_check

#enable_debug=1
#enable_save_to_file=0

#if ir_receiver_check.check_ir():
	#print("Disable IR receiver before continuing")
	#exit()
	
#ser = serial.Serial('/dev/ttyAMA0',  9600, timeout = 0)	#Open the serial port at 9600 baud
#ser.flush()

#def cleanstr(in_str):
	#out_str = "".join([c for c in in_str if c in "0123456789.-" ])
	#if len(out_str)==0:
		#out_str = "-1"
	#return out_str

#def safefloat(in_str):
	#try:
		#out_str = float(in_str)
	#except ValueError:
		#out_str = -1.0
	#return out_str

#class GPS:
	##The GPS module used is a Grove GPS module http://www.seeedstudio.com/depot/Grove-GPS-p-959.html
	#inp=[]
	## Refer to SIM28 NMEA spec file http://www.seeedstudio.com/wiki/images/a/a0/SIM28_DATA_File.zip
	#GGA=[]


	##Read data from the GPS
	#def read(self):	
		#while True:
			#GPS.inp=ser.readline()
			#if GPS.inp[:6] =='$GPGGA': # GGA data , packet 1, has all the data we need
				#break
			#time.sleep(0.1)     #without the cmd program will crash
		#try:
			#ind=GPS.inp.index('$GPGGA',5,len(GPS.inp))	#Sometimes multiple GPS data packets come into the stream. Take the data only after the last '$GPGGA' is seen
			#GPS.inp=GPS.inp[ind:]
		#except ValueError:
			#print ("")
		#GPS.GGA=GPS.inp.split(",")	#Split the stream into individual parts
		#return [GPS.GGA]
		
	##Split the data into individual elements
	#def vals(self):
		#if enable_debug:
			#print(GPS.GGA)
			
		#time=GPS.GGA[1]
		
		#if GPS.GGA[2]=='':  # latitude. Technically a float
			#lat =-1.0
		#else:
			#lat=safefloat(cleanstr(GPS.GGA[2]))
		
		#if GPS.GGA[3]=='':  # this should be either N or S
			#lat_ns=""
		#else:
			#lat_ns=str(GPS.GGA[3])
			
		#if  GPS.GGA[4]=='':  # longitude. Technically a float
			#long=-1.0
		#else:
			#long=safefloat(cleanstr(GPS.GGA[4]))
		
		#if  GPS.GGA[5]=='': # this should be either W or E
			#long_ew=""
		#else:
			#long_ew=str(GPS.GGA[5])
			
		#fix=int(cleanstr(GPS.GGA[6]))
		#sats=int(cleanstr(GPS.GGA[7]))
		
		#if  GPS.GGA[9]=='':
			#alt=-1.0
		#else:
			## change to str instead of float
			## 27"1 seems to be a valid value
			#alt=str(GPS.GGA[9])
		#return [time,fix,sats,alt,lat,lat_ns,long,long_ew]
	
	## Convert to decimal degrees
	#def decimal_degrees(self, raw_degrees):
		#try:
			#degrees = float(raw_degrees) // 100
			#d = float(raw_degrees) % 100 / 60
			#return degrees + d
		#except: 
			#return raw_degrees


#if __name__ == "__main__":
	#g=GPS()
	#if enable_save_to_file:
		#f=open("gps_data.csv",'w')	#Open file to log the data
		#f.write("name,latitude,longitude\n")	#Write the header to the top of the file
	#ind=0
	#while True:
		#time.sleep(0.01)
		#try:
			#x=g.read()	#Read from GPS
			#[t,fix,sats,alt,lat,lat_ns,longitude,long_ew]=g.vals()	#Get the individial values
				
			## Convert to decimal degrees
			#if lat !=-1.0:
				#lat = g.decimal_degrees(safefloat(lat))
				#if lat_ns == "S":
					#lat = -lat

			#if longitude !=-1.0:
				#longitude = g.decimal_degrees(safefloat(longitude))
				#if long_ew == "W":
					#longitude = -longitude
					
			## print ("Time:",t,"Fix status:",fix,"Sats in view:",sats,"Altitude",alt,"Lat:",lat,lat_ns,"Long:",long,long_ew)
			#try:
				#print("Time\t\t: %s\nFix status\t: %d\nSats in view\t: %d\nAltitude\t: %s\nLat\t\t: %f\nLong\t\t: %f") %(t,fix,sats,alt,lat,longitude)
			#except:
				#print("Time\t\t: %s\nFix status\t: %s\nSats in view\t: %s\nAltitude\t: %s\nLat\t\t: %s\nLong\t\t: %s") %(t,str(fix),str(sats),str(alt),str(lat),str(longitude))
				
			#s=str(t)+","+str(safefloat(lat)/100)+","+str(safefloat(longitude)/100)+"\n"	
				
			#if enable_save_to_file:
				#f.write(s)	#Save to file
			#time.sleep(2)
		#except IndexError:
			#print ("Unable to read")
		#except KeyboardInterrupt:
			#if enable_save_to_file:
				#f.close()
			#print ("Exiting")
			#sys.exit(0)  






import grovepi
import serial, time, sys
import re

en_debug = True

def debug(in_str):
	if en_debug:
		print(in_str)

patterns=["$GPGGA",
	"/[0-9]{6}\.[0-9]{2}/", # timestamp hhmmss.ss
	"/[0-9]{4}.[0-9]{2,/}", # latitude of position
	"/[NS]",  # North or South
	"/[0-9]{4}.[0-9]{2}", # longitude of position
	"/[EW]",  # East or West
	"/[012]", # GPS Quality Indicator
	"/[0-9]+", # Number of satellites
	"/./", # horizontal dilution of precision x.x
	"/[0-9]+\.[0-9]*/" # altitude x.x
	]

class GROVEGPS():
	def __init__(self,port='/dev/ttyAMA0',baud=9600,timeout=0):
		self.ser = serial.Serial(port,baud,timeout=timeout)
		self.ser.flush()
		self.raw_line = ""
		self.gga = []
		self.validation =[] # contains compiled regex

		# compile regex once to use later
		for i in range(len(patterns)-1):
			self.validation.append(re.compile(patterns[i]))

		self.clean_data()
		# self.get_date()  # attempt to gete date from GPS. 

	def clean_data(self):
		'''
		clean_data: 
		ensures that all relevant GPS data is set to either empty string
		or -1.0, or -1, depending on appropriate type
		This occurs right after initialisation or
		after 50 attemps to reach GPS
		'''
		self.timestamp = ""
		self.lat = -1.0    # degrees minutes and decimals of minute
		self.NS = ""
		self.lon = -1.0
		self.EW = ""
		self.quality = -1
		self.satellites = -1
		self.altitude = -1.0

		self.latitude = -1.0  #degrees and decimals
		self.longitude = -1.0
		self.fancylat = ""  #
		
	def get_date(self):
		'''
		attempt to get date from GPS data. So far no luck. GPS does
		not seem to send date sentence at all
		function is unfinished
		'''
		valid = False
		for i in range(50):
			time.sleep(0.5)
			print i
			self.raw_line = self.ser.readline().strip()
			if self.raw_line[:6] == "GPZDA":  # found date line!
				print 
				print self.raw_line
			

	def read(self):
		'''
		Attempts 50 times at most to get valid data from GPS
		Returns as soon as valid data is found
		If valid data is not found, then clean up data in GPS instance
		'''
		valid = False
		for i in range(50):
			time.sleep(0.5)
			self.raw_line = self.ser.readline().strip()
			if self.validate(self.raw_line):
				valid = True
				break;
		
		if valid:
			return self.gga
		else:
			self.clean_data()
			return []

	def validate(self,in_line):
		'''
		Runs regex validation on a GPGAA sentence. 
		Returns False if the sentence is mangled
		Return True if everything is all right and sets internal
		class members.
		'''
		if in_line == "":
			return False
		if in_line[:6] != "$GPGGA":
			return False

		self.gga = in_line.split(",")
		debug (self.gga)

		#Sometimes multiple GPS data packets come into the stream. Take the data only after the last '$GPGGA' is seen
		try:
			ind=self.gga.index('$GPGGA',5,len(self.gga))	
			self.gga=self.gga[ind:]
		except ValueError:
			pass

		if len(self.gga) != 15:
			debug ("Failed: wrong number of parameters ")
			debug (self.gga)
			return False
		
		for i in range(len(self.validation)-1):	
			if len(self.gga[i]) == 0:
				debug ("Failed: empty string %d"%i)
				return False
			test = self.validation[i].match(self.gga[i])
			if test == False:
				debug ("Failed: wrong format on parameter %d"%i)
				return False
			else:
				debug("Passed %d"%i)

		try:
			self.timestamp = self.gga[1]
			self.lat = float(self.gga[2])
			self.NS = self.gga[3]
			self.lon = float(self.gga[4])
			self.EW = self.gga[5]
			self.quality = int(self.gga[6])
			self.satellites = int(self.gga[7])
			self.altitude = float(self.gga[9])

			self.latitude = self.lat // 100 + self.lat % 100 / 60
			if self.NS == "S":
				self.latitude = - self.latitude
			self.longitude = self.lon // 100 + self.lon % 100 / 60
			if self.EW == "W":
				self.longitude = -self.longitude
		except ValueError:
			debug( "FAILED: invalid value")

		return True


if __name__ =="__main__":
	gps = GROVEGPS()
	while True:
		time.sleep(2)
		in_data = gps.read()
		if in_data != []:
			print ("pinta",in_data)
