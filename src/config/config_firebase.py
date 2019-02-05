from pyrebase import pyrebase


#FIREBASE----------------------------------------------------
config = {
  'apiKey': 'AIzaSyCpUNH5reSxyo1fwiBUu1-DnJCTFBAO_e8',
  'authDomain': 'carsens-80cc6.firebase.com',
  'databaseURL': 'https://carsens-80cc6.firebaseio.com/',
  'storageBucket': 'carsens-80cc6.appspot.com',
  "serviceAccount": "data.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
