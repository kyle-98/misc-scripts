# pip install opencv-python pyzbar pillow
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import cv2
from pyzbar.pyzbar import decode
import os


class ThePrimeExpress:
    def __init__(self, root):
        self.root = root
        self.root.title("The Prime Express")

        self.label = tk.Label(root, text="Click to open one or more images and decode")
        self.label.pack(pady=10)

        self.open_button = tk.Button(root, text="Open Image(s)", command=self.open_images)
        self.open_button.pack(pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10)

    def open_images(self):
        filepaths = filedialog.askopenfilenames(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if filepaths:
            self.decode_multiple_qr_codes(filepaths)

    def decode_multiple_qr_codes(self, filepaths):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        output_file = os.path.join(script_dir, "output.txt")

        all_qr_data = "" 
        
        for filepath in filepaths:
            img = cv2.imread(filepath)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            qr_codes = decode(gray)
            if qr_codes:
                for qr_code in qr_codes:
                    qr_data = qr_code.data.decode("utf-8")
                    all_qr_data += qr_data  
            else:
                self.result_label.config(text="No QR Code found in one of the images.")
        
        with open(output_file, "w") as file:
            file.write(all_qr_data)

        self.result_label.config(text=f"Decoded QR Codes combined: {all_qr_data}")

        messagebox.showinfo("Success", "QR codes decoded and combined into output.txt")


if __name__ == "__main__":
    root = tk.Tk()
    app = ThePrimeExpress(root)
    root.mainloop()
