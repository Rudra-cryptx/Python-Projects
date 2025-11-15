import qrcode 
data = input("Enter text or url to generate QR code: ").strip()
filename = input("Enter the file name: ").strip()
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
image = qr.make_image(fill='black', back_color='white')
image.save(f"{filename}.png")
print(f"QR code saved as {filename}.png")