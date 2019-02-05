import pyrebase


#FIREBASE----------------------------------------------------
config = {
  'apiKey': 'AIzaSyBzGumeyc8y6CnoebtwZhJ3t52lkMFXMuk',
  'authDomain': 'carsens-9edc7.firebase.com',
  'databaseURL': 'https://carsens-9edc7.firebaseio.com/',
  'storageBucket': 'carsens-9edc7.appspot.com'
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
