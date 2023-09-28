import customtkinter as ctk
import time


class GuiClock(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Clock")

        self.label = ctk.CTkLabel(self, font=("Arial", 80), text="")
        self.label.pack(padx=20, pady=20, fill=ctk.BOTH, expand=True)

        self.__update_time()

        self.mainloop()

    def __update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.configure(text=current_time)
        self.after(1000, self.__update_time)
