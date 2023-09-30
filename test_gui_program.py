import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk
import customtkinter as ctk


class TestGuiProgram(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.menu_bar_enabled = True

        self.title("Test GUI Program")
        self.geometry("1280x720")
        self.resizable(False, False)
        ctk.set_default_color_theme("blue")
        self._set_appearance_mode('dark')

        if self.menu_bar_enabled:
            self.menubar = tk.Menu(self)
            menus = [
                {"label": "File", "options": [
                    {"label": "Close", "command": exit}
                ]}
            ]
            for menu in menus:
                file_menu = tk.Menu(self.menubar, tearoff=0)
                for option in menu["options"]:
                    file_menu.add_command(label=option["label"], command=option["command"])
                self.menubar.add_cascade(menu=file_menu, label=menu["label"])
            self.config(menu=self.menubar)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        side_bar_width = 200
        self.side_bar = ctk.CTkFrame(
            self,
            width=side_bar_width,
            height=self._current_height,
            fg_color='#202020',
            corner_radius=0
        )
        self.side_bar.grid(column=0, row=0, sticky='w')

        # self.button = ctk.CTkButton(self.side_bar, text="Button")
        # self.button.pack()

        self.content = ctk.CTkFrame(
            self,
            width=self._current_width - side_bar_width,
            height=self._current_height,
            fg_color='#222222',
            corner_radius=0
        )
        self.content.grid(column=1, row=0, sticky='e')

        # self.header = ctk.CTkFrame(self, fg_color='orange', height=50, corner_radius=0)
        # self.header.pack(side='top', fill='x')
        #
        # self.header_label = ctk.CTkLabel(self.header, text="Header", font=self.__get_font(18), text_color='black')
        # self.header_label.pack()

        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        # self.grid_rowconfigure((0, 1, 2), weight=1)
        #
        # self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        # self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        # self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="CustomTkinter",
        #                                font=ctk.CTkFont(size=20, weight="bold"))
        # self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        #
        # for i in range(3):
        #     btn = ctk.CTkButton(self.sidebar_frame)
        #     btn.grid(row=i + 1, column=0, padx=20, pady=10)
        #
        # self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        # self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        # self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame,
        #                                                      values=["Light", "Dark", "System"])

        self.mainloop()

    def __get_font(self, size):
        return "Arial", size
