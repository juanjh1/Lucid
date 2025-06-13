import customtkinter as ctk

    
class TextFrame(ctk.CTkFrame):
    def __init__(self,parent ):
        super().__init__(parent, fg_color="white", corner_radius=0 )
        self.place(relx=0, rely=0.05, relheight=0.95, relwidth=1, anchor="nw")

