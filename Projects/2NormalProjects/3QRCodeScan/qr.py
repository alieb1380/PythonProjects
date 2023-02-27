import pyqrcode 
from pyqrcode import QRCode 

# String which represent the QR code 
user_input = input("Enter your URL: ")

# Generate QR code 
url = pyqrcode.create(user_input) 

# Create and save the png file naming "myqr.png" 
url.svg("myyoutube.svg", scale = 8) 