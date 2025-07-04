import pyrebase
import random
import time


config = {
  "apiKey": "AIzaSyAamS-omT7i-1fFFuwHr5k8_ILt0ptNl3E",
  "authDomain": "pidrowsiness-277a4.firebaseapp.com",
  "databaseURL": "https://pidrowsiness-277a4-default-rtdb.firebaseio.com",
  "projectId": "pidrowsiness-277a4",
  "storageBucket": "pidrowsiness-277a4.appspot.com",
  "messagingSenderId": "443787716450",
  "appId": "1:443787716450:web:c7033070895e50b0e56e3b",
  "measurementId": "G-KBBZSE34Y3"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

while True:
  data = {
    "AlertTime": random.randrange(1, 10),
  }

  db.child("Status").set(data)

  # Add a 5-second delay between pushes
  time.sleep(1)
  print(data)
