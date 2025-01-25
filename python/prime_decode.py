import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from pyzbar.pyzbar import decode
import os

def upload_and_decode_multiple():
    file_paths = filedialog.askopenfilenames(title="Select images", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    
    if file_paths:
        full_decoded_text = ""  
        for file_path in file_paths:
            img = Image.open(file_path)
            
            decoded_objects = decode(img)
            
            if decoded_objects:
                for obj in decoded_objects:
                    qr_data = obj.data.decode('utf-8')
                    full_decoded_text += qr_data 
            else:
                result_label.config(text="One or more images have no QR code.")
        
        output_file = os.path.join(os.path.dirname(__file__), "output.txt")
        with open(output_file, "w") as file:
            if full_decoded_text == '':
                messagebox.showinfo('Failure', 'Failed to detect QR code in photo')
            else:
                file.write(full_decoded_text)
        
        if full_decoded_text != '':
            result_label.config(text="Decoded text written to output.txt")

root = tk.Tk()
root.geometry('400x150')
root.title("The Prime Express")

upload_button = tk.Button(root, text="Upload Image(s)", command=upload_and_decode_multiple)
upload_button.pack(pady=20)

result_label = tk.Label(root, text="Decoded text will appear here", wraplength=300)
result_label.pack(pady=20)

root.mainloop()
