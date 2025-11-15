# 📱 QR Code Generator (Python)

This project is a simple and beginner-friendly Python program that generates a QR code from any text or URL entered by the user.  
The QR code is then saved as a **PNG image** in the same directory.

---

## 🚀 Features

- Generate QR codes from:
  - Plain text  
  - Website URLs  
  - Email IDs  
  - Phone numbers  
  - Any custom string  
- Saves the QR code as `<filename>.png`
- Uses Python's `qrcode` library
- Clean and minimal code
- Automatically fits long data inside the QR code

---

## 🧠 How It Works

1. The user enters any input text or URL.
2. A QRCode object is created.
3. The input data is added using `add_data()`.
4. The QR generator converts the data into a QR matrix.
5. The QR image is generated.
6. The image is saved with the given filename.

---

## 📂 Full Source Code

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
Enter the file name: github_qr
QR code saved as github_qr.png


📦 Requirements
pip install qrcode[pil]


🔧 Understanding the Key Functions
✔ qrcode.QRCode()

Creates a QRCode object with parameters like version, box size, and border.

✔ add_data(data)

Adds your text or URL into the QR code.

✔ make(fit=True)

Automatically adjusts the QR code to fit the given data.

✔ make_image()

Generates the final QR image.


🔗 Important Tips for URL QR Codes

To ensure QR scanners correctly open your link:

✔ Correct:https://www.google.com

❌ Incorrect:
www.google.com
google.com
