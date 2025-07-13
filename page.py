
import customtkinter as ctk


class BasicPage(ctk.CTkFrame):
    def __init__(self, name, master, window_config=None, *args, **kwargs):
        super().__init__(master=master)
        self.name = name
        self.active = False
        self.window_config = window_config or {}

class ScrollablePage(ctk.CTkScrollableFrame):
    def __init__(self, name, master, window_config=None, *args, **kwargs):
        super().__init__(master=master)
        self.name = name
        self.active = False
        self.window_config = window_config or {}
