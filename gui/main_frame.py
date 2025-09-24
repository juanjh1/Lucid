import customtkinter as ctk


class MainFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent, fg_color="blue", corner_radius=0 )
        self.place(relx=0, rely=0.05, relheight=0.90, relwidth=1, anchor="nw")
        
        self.tab = TabMainFrame(self)
        self.textframe = TextFrame(self)

    def get_tab_main_frame(self):
        return self.tab
    def get_text_frame(self):
        return self.textframe

class TabMainFrame(ctk.CTkFrame):
    TABS = {}
    def __init__(self,parent):
        super().__init__(parent, fg_color="white", corner_radius=0 )
        self.place(relx=0, rely=0, relheight=0.05, relwidth=1, anchor="nw")
    
class TextFrame(ctk.CTkFrame):
    def __init__(self,parent ):
        super().__init__(parent, fg_color="white", corner_radius=0 )
        self.place(relx=0, rely=0.05, relheight=0.95, relwidth=1, anchor="nw")
 
