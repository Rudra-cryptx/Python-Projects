# 📱 QR Code Generator (Python)

This is a simple Python program that generates a QR code from any text or URL entered by the user.  
The generated QR code is saved as a **PNG file** in the same folder.

---

## 🚀 Features
- Generate QR codes from:
  - Text  
  - Website URLs  
  - Email addresses  
  - Phone numbers  
- Saves the QR code as an image (`.png`)
- Simple and beginner-friendly script
- Uses the `qrcode` Python library

---

## 🧠 How It Works
1. The user enters any text or URL.
2. A QRCode object is created using the `qrcode` module.
3. `add_data()` stores the text or URL into the QR code.
4. The code is converted into an image and saved.
5. The user gets a confirmation message.

---

## 📄 Code

```python
import qrcode as qr

data = input("Enter text or URL to generate QR code: ").strip()
filename = input("Enter the file name: ").strip()

qr_code = qr.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr_code.add_data(data)
qr_code.make(fit=True)

image = qr_code.make_image(fill='black', back_color='white')
image.save(f"{filename}.png")

print(f"QR code saved as {filename}.png")


🧪 Example Usage
Enter text or URL to generate QR code: https://github.com/rudra
Enter the file name: Rudra git hub QR code
QR code saved as Rudra git hub QR code.png


📦 Requirements

Install the qrcode module: pip install qrcode[pil]

🔗 Tips for URL QR Codes

To ensure the QR redirects correctly, always include:
https://

Example:

✔ Correct → https://www.google.com
❌ Incorrect → www.google.com