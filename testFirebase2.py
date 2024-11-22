import pyrebase
import random
import time

config = {
  "apiKey": "AIzaSyAamS-omT7i-1fFFuwHr5k8_ILt0ptNl3E",  # Use double quotes for key names
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

# Get the latest AlertTime from Firebase (replace "Status" with your actual path)
latest_alert_time_ref = db.child("Status").order_by_key().limit_to_last(1)  # Get the last child
latest_alert_time_data = latest_alert_time_ref.get().val()

# ... (Firebase retrieval code)

# Initialize with default value
latest_alert_time = 0

if latest_alert_time_data is not None:
    # Check if "AlertTime" key exists
    if "AlertTime" in latest_alert_time_data:
        latest_alert_time = latest_alert_time_data["AlertTime"]  # Extract from "AlertTime" key
    else:
        print("No 'AlertTime' key found in retrieved data, using default 0.")
else:
    print("No existing AlertTime found in database, using default 0.")




while True:
  latest_alert_time += 1
  data = {
    "AlertTime": latest_alert_time
  }

  db.child("Status").push(data)  #Use push() for adding unique child nodes
  db.update(data)  # Remove this line if you only want to push data to "Status"
  break


