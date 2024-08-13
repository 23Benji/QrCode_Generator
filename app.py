import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
import qrcode
import os
import glob


# Function to create QR code and save in "QrCodes" folder
def generate_qrcode(text):

    # Create the "QrCodes" directory if it doesn't exist
    os.makedirs("QrCodes", exist_ok=True)

    # Save the QR code in the "QrCodes" folder
    filename = os.path.join("QrCodes", f"{text.replace(' ', '_')}.png")
    img = qrcode.make(text)
    filename.replace('/','')
    img.save(filename)

    # Load and display the image
    image = Image.open(filename)
    image = ImageTk.PhotoImage(image)

    # Update the label with the new image
    image_label.config(image=image)
    image_label.image = image  # Keep a reference to avoid garbage collection


# Function to delete all PNG files in the "QrCodes" folder
def delete_qrcodes():
    files = glob.glob("QrCodes/*.png")
    for f in files:
        os.remove(f)
    print("All QR code images deleted.")


# Initialize the Tkinter app with ttkbootstrap theme
app = ttk.Window(themename="darkly")  # Change the theme for a modern look
app.title("QR Code Generator")
app.resizable(False, False)

input_Var = tk.StringVar()

# Create the UI elements with improved styling
txt_Label = ttk.Label(app, text='Welcome to the QRCode Generator!',
                      font=('Calibri', 22, 'bold'),
                      bootstyle="primary")
txt_Label.pack(pady=(30, 10))

description = ttk.Label(app, text="Create your custom QR Code with one click!",
                        font=('Calibri', 14),
                        bootstyle="light")
description.pack(pady=(0, 20))

txt_entry = ttk.Entry(app, textvariable=input_Var,
                      font=('Calibri', 15),
                      width=30,
                      bootstyle="info")
txt_entry.pack(pady=(0, 20))

gen_Button = ttk.Button(app, text='Generate',
                        command=lambda: generate_qrcode(input_Var.get()),
                        bootstyle="success-outline")
gen_Button.pack(pady=10)

del_Button = ttk.Button(app, text='Delete All QR Codes',
                        command=delete_qrcodes,
                        bootstyle="danger-outline")
del_Button.pack(pady=10)

image_label = ttk.Label(app)
image_label.pack(pady=(30, 0), padx=10)

app.mainloop()
