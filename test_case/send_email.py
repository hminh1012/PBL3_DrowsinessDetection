import smtplib
from email.message import EmailMessage
import datetime
import pytz
import json
from urllib.request import urlopen

# open following url to get ipaddress
urlopen("http://ipinfo.io/json")

# load data into array
data = json.load(urlopen("http://ipinfo.io/json"))

# extract lattitude
lat = data['loc'].split(',')[0]

# extract longitude
lon = data['loc'].split(',')[1]

print(lat, lon)
 
# using now() to get current time
current_time = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))

# set email address
from_email_addr ="pidrowsiness@gmail.com" #REPLACE_WITH_THE_SENDER_EMAIL
from_email_pass ="duqj osfv jkkq lxsv"#REPLACE_WITH_THE_SENDER_EMAIL_APP_PASSWORD
to_email_addr ="starsrising8888@gmail.com"#REPLACE_WITH_THE_RECIPIENT_EMAIL

# Create a message object
msg = EmailMessage()


# Set the email body
body = "Dear Da Nang Police Department,\n\nThis email is an automated notification from a driver drowsiness detection system. Our system has identified a potential case of driver drowsiness involving the following vehicle:\nVehicle Type: Car\nLicense Plate: 00000000\n\nThe system detected signs of drowsiness on " + str(current_time.strftime("%B")) + " " + str(current_time.day) + "th at " + str(current_time.hour) + " o'clock, while the vehicle was located in Da Nang, Vietnam.\n\nPlease note: This is an automated alert and does not necessarily confirm driver drowsiness.\nWe recommend that you investigate this incident at your discretion. The following information may be helpful for your investigation:\n\nThe vehicle's last known location:\nLatitude: " + str(lat) + "\nLongitude: " + str(lon) + "\nTime of the alert: " + current_time.strftime("%c") + "\nWe urge you to take appropriate action to ensure the safety of the driver and others on the road.\n\nThank you for your cooperation.\nSincerely,\n[PBL3 21ECE Group4]"
msg.set_content(body)


# Set sender and recipient
msg['From'] = from_email_addr
msg['To'] = to_email_addr


# Set your email subject
msg['Subject'] = 'Drowsy Driver Alert - [21ECE Group 4] - Da Nang, Vietnam'


# Connecting to server and sending email
# Edit the following line with your provider's SMTP server details
server = smtplib.SMTP('smtp.gmail.com', 587)

# Comment out the next line if your email provider doesn't use TLS
server.starttls()
# Login to the SMTP server
server.login(from_email_addr, from_email_pass)

# Send the message
server.send_message(msg)

print('Email sent')

#Disconnect from the Server
server.quit()
