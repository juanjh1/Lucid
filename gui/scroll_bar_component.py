import customtkinter as ctk

class ScrollBar (ctk.CTkFrame):
    SCROLL_BAR_WIDTH = 15
    def __init__(self,parent):
        super().__init__(parent, fg_color="violet", corner_radius=0, width=ScrollBar.SCROLL_BAR_WIDTH, )