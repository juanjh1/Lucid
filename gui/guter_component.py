import customtkinter as ctk

class Gutter(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#4378a2", corner_radius=0)