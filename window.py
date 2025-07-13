
import customtkinter as ctk
from dev.page import BasicPage

class Window(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.pages = []
        self.active_page = None
        self.previous_page = None

    def add_page(self, page: BasicPage):
        self.pages.append(page)
    
    def switch_page(self, page_name: str):
        self.active_page = None
        
        for page in self.pages:
            if page.name == page_name:
                self.active_page = page
                break

        if self.active_page:
            self.build_active_page()
    
    def build_active_page(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.active_page.grid(row=0, column=0, sticky="nwse")
    
    def destroy_previous_page(self):
        if self.previous_active_page:
            if self.previous_active_page.winfo_exists():
                self.previous_active_page.destroy()