import customtkinter as ctk
from core.options_controller import OptionController


class NabItemButton (ctk.CTkButton):
    def __init__(self,parent, text, command):
        super().__init__(parent,corner_radius=0, command=command, width=60, text=text)
