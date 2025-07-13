
import customtkinter as ctk


class BasicPage(ctk.CTkFrame):
    def __init__(self, name, master, *args, **kwargs):
        super().__init__(master=master)
        self.name = name
        self.active = False