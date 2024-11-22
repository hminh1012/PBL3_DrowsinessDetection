import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase configuration (replace with your own credentials)
cred = credentials.Certificate('serviceAccount.json')  # Replace with your credentials file path
firebase_admin.initialize_app(cred, {
  'databaseURL': 'https://pidrowsiness-277a4-default-rtdb.firebaseio.com/'
})

# Get a reference to the database
ref = db.reference('your_database_path')  # Replace with your desired path in the database

# Get the number to send (replace with your logic to obtain the number)
number = 123  # Example number, replace with your actual logic

# Push the number to the database
ref.push(number)

print('Number sent to Firebase Realtime Database successfully!')
