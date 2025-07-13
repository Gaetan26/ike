
import customtkinter as ctk
from dev.page import BasicPage

class Window(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.pages = []
        self.active_page = None
        self.previous_page = None
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def add_page(self, page: BasicPage):
        self.pages.append(page)
        page.grid()
        page.grid_remove()
    
    def switch_page(self, page_name: str):
        for page in self.pages:
            if page.name == page_name:
                self.previous_page = self.active_page
                self.active_page = page
                page.active = True
        
        if self.previous_page and self.previous_page in self.pages:
            self.previous_page.grid_remove()
            self.previous_page.active = False
        
        self.apply_window_config(self.active_page.window_config)
        self.active_page.grid(row=0, column=0, sticky="nwse")
    
    def apply_window_config(self, config: dict):
        for param, value in config.items():
            method = getattr(self, param, None)

            if callable(method):
                try:
                    if isinstance(value, dict):
                        method(**value)
                    else:
                        method(value)
                except TypeError as e:
                    print(f"call error: self.{param}({value}) → {e}")
            else:
                print(f"method not found: self.{param}")
            