# Import QRCode from pyqrcode
import pyqrcode
import qrtools
import png
from pyqrcode import QRCode

#face-smiling
facesmiling='\U0001F600'
# String which represents the QR code
s = input("Enter any data")
# Generate QR code 
url = pyqrcode.create(s)
# Create and save the png file naming "myqr.png"
url.png('qr_file.png', scale = 6)
print("Your qr file is created as qr_file.png\t\t"+facesmiling)
dataOut = input("Do you want to read the qr file ?\n Press Y for YES and \n N for NO\n Your Choice(Y/N) : ")
if dataOut == "Y":
    print(facesmiling+facesmiling+"reading data from qr "+facesmiling+facesmiling)
    print("\n\n")
    print(url.data)
else:
    print("Thank you!!")

