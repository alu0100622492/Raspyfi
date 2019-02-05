
#from firebase import firebase

#fb = firebase('https://carsens-9edc7.firebaseio.com/', None)
###ESCUCHA
## setup a database reference at path /channels/channelId
#channel = firebase.database().ref('/testbal' + 7)
# add a listener to the path that fires any time the value of the data changes
#channel.on('value', function(data) {
  #onMessage(data.val());
#});


## Sample callback function
#def p(x):
    #print x

## Firebase object
#fb = firebase('https://carsens-9edc7.firebaseio.com/', None)

## Add listener to colors child with no callback
#no_callback = fb.child("/sensores").listener()

## Or use a custom callback
#custom_callback = fb.child("testbal").listener(p)

## Start and stop the stream using the following
#custom_callack.start()
#raw_input("ENTER to stop...")
#custom_callback.stop()



#from firebase import firebase


#firebase = firebase.FirebaseApplication('https://carsens-9edc7.firebaseio.com/', None)

#result = firebase.get('/sensores', None)

#print result


### actualizar dato o lo crea si no esta creado
#firebase.put('/sensores','testval',0)
#firebase.put('/sensores','termometro',9.0)
###firebase.child_added('/sensores','ventana',0)
###firebase.push('https://carsens-9edc7.firebaseio.com/', 'ventana',1)

#users = firebase.child('/sensores')
##print users


import pyrebase


def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}



config = {
  'apiKey': 'AIzaSyBzGumeyc8y6CnoebtwZhJ3t52lkMFXMuk',
  'authDomain': 'carsens-9edc7.firebase.com',
  'databaseURL': 'https://carsens-9edc7.firebaseio.com/',
  'storageBucket': 'carsens-9edc7.appspot.com'
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
salida = db.child('/sensores').get()
print salida.val()

#hola = db.child('/sensores').child('testbal').get()
 #hola1 = db.child('/sensores').child('/acelerometro').child('x').set(7)
 
#print hola1.val()
##hola1 = db.child('/sensores').child('testbal').set(7)
db.child('/sensores').update({'testbal': 6})

mystream = db.child('/sensores').child('testbal').stream(stream_handler,None)
#mystream.close()
#db.child('/sensores').child('testbal').listener()

#db.on('value', def(data):
          #print("data",data.val())
#)
    

