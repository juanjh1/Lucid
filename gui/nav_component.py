import customtkinter as ctk

from  core.nav_item_controller import NavItemButtonComponent

class NavMenu(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent, corner_radius=0)

        self.nav_item_button = NavItemButtonComponent(self, parent.options_adapter(), "File")
        self.nav_item_button.pack(side="left")

