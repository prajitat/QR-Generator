import urllib.request
import urllib.parse
from datetime import datetime

def generate_qr():
    # Get user input
    data = "https://prajita.vercel.app/"
    if not data:
        print("Error: No data was provided. Please enter a valid text or a URL!")
        return

    #Specify the color and background color
    foreground_color = "FF69B4" # PINK 
    background_color = "FFFFFF" # WHITE
    qr_url = f"http://api.qrserver.com/v1/create-qr-code/?data={urllib.parse.quote(data)}&size=200*200&color={foreground_color}&bgcolor={background_color}"

    try:
        response = urllib.request.urlopen(qr_url)
        with open("newgr.png", "wb") as img_file:
            img_file.write(response.read())
        print("QR code has been generated!")
    except Exception as e:
        print(f"Error: {e}")

# Run the function
generate_qr()



