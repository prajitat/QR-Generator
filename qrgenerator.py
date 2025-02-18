import qrcode
from datetime import datetime

def generate_qr():
    #Get user input for the QR code content
    data = input("Enter the data for the QR code (URL/Text): ").strip()

if not data:
    print("Error: No data was provided. Please enter valid text or a URL.")
    return

# Create a QR code instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
)

# Add data to the QR code

data = "https://prajita.vercel.app"
qr.add_data(data)
qr.make(fit = True)



img = qr.make_image(fill='black', back_color = 'white')
img.save("newqr.png")

print("QR code has been generated.")
