import customtkinter as ctk
from core.nav_menu_controller import NavController 
from core.editor_frame import MainEditorFrameController
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
#from utils.dialog_utils import create_frame
from utils.adapters.app_adapters import AppAdapeterToFileOption

class App(TkinterDnD.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)      
        self.geometry(f"{self.winfo_screenwidth() - 100}x{self.winfo_screenheight()}+0+0")
        #self.drop_target_register(DND_FILES)
        #self.dnd_bind('<<Drop>>', self.drop_event)
        #self.overrideredirect(True)
        
        self.main_frame = MainEditorFrameController(self)
        self.main_frame.place(relx=0, rely=0.05, relheight=0.90, relwidth=1, anchor="nw")
        self.menu = NavController(self).place(relx=0, rely=0.0, relheight=0.05, relwidth=1, anchor="nw")
    def set_frame_in_main_app(self, object):
            return object(self)
    
    def options_adapter(self):
         return AppAdapeterToFileOption(self)
    
    # def drop_event(self, event):
    #     file_path = event.data
    #     create_frame(main_frame=self.get_main_frame().get_text_frame(), 
    #                 tab_section =self.get_main_frame().get_tab_main_frame(),
    #                  path = file_path )
    def create_view(self):
         self.main_frame.create_new_view()

if __name__ == "__main__":
    app =App("Lucid")
    app.mainloop()