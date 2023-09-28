import qrcode
import customtkinter as ctk
import tkinter as tk
from PIL import ImageTk


class QRCodeGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.img = ''
        self.label = None

        self.title("QR Code Generator")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

        self.input = ctk.CTkEntry(self)
        self.input.grid(column=0, row=1, padx=10, pady=10)
        self.input.bind('<Return>', self.__generate_qr_code)

        self.button = ctk.CTkButton(self, text="Generate", command=self.__generate_qr_code)
        self.button.grid(column=0, row=2, padx=10, pady=10)

        self.mainloop()

    def __generate_qr_code(self, event):
        qr_code = qrcode.QRCode(version=1)
        qr_code.add_data(self.input.get())
        qr_code.make(fit=True)
        img = qr_code.make_image(fill='black', back_color='white')
        self.img = ImageTk.PhotoImage(img)
        self.label = tk.Label(image=self.img)
        self.label.grid(column=0, row=0, padx=10, pady=10)
