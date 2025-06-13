import customtkinter as ctk

class TabMainFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent, fg_color="#4378a2", corner_radius=0 )
        self.place(relx=0, rely=0, relheight=0.05, relwidth=1, anchor="nw")
    