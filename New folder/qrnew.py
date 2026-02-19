import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from datetime import datetime

# Create output folder
output_folder = "generated_qr"
os.makedirs(output_folder, exist_ok=True)

count = 1

def generate_qr():
    global count
    
    mobile_number = entry.get().strip()

    if mobile_number == "":
        messagebox.showerror("Error", "Please enter a mobile number")
        return

    # Format as telephone QR
    data = f"tel:{mobile_number}"

    # Create QR Code
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"qr_{mobile_number}_{timestamp}.png"
    file_path = os.path.join(output_folder, filename)

    img.save(file_path)

    # Show preview
    preview = Image.open(file_path)
    preview = preview.resize((200, 200))
    img_tk = ImageTk.PhotoImage(preview)

    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    messagebox.showinfo("Success", f"QR Code saved as:\n{file_path}")

    entry.delete(0, tk.END)
    count += 1


# GUI Setup
root = tk.Tk()
root.title("Mobile Number QR Generator")
root.geometry("350x450")
root.resizable(False, False)

tk.Label(root, text="Enter Mobile Number", font=("Arial", 14)).pack(pady=15)

entry = tk.Entry(root, width=25, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Generate QR Code", command=generate_qr,
          bg="blue", fg="white", font=("Arial", 12)).pack(pady=15)

qr_label = tk.Label(root)
qr_label.pack(pady=20)

tk.Label(root, text="QR Codes saved in 'generated_qr' folder",
         font=("Arial", 9)).pack(side="bottom", pady=10)

root.mainloop()
