import qrcode

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
)

data = "https://prajita.vercel.app"
qr.add_data(data)
qr.make(fit = True)

img = qr.make_image(fill='black', back_color = 'white')
img.save("newqr.png")

print("QR code has been generated.")
