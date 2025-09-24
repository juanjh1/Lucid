import customtkinter as ctk

class TextFrame(ctk.CTkScrollableFrame):
    def __init__(self,parent):
        super().__init__(parent, fg_color="pink", corner_radius=0 )
        

    #     #canvas_manager
    #     self.canvas = tk.Canvas(self)
    #     self.canvas.update_idletasks()
    #     self.canvas.pack(expand=True, fill="both")
        
    #     #components
        
    #     self.text_box = TextBox(self.canvas, path)
    #     self.guter = Gutter(self.canvas, self.text_box)
    #     self.scroll = ScrollContainer(self.canvas, self.text_box)
    #     self.tab_frame = None

    #     #events
    #     self.text_box.bind("<<Modified>>", lambda event: self.on_modified())  
        
    #     #layout
    #     self.place(relx=0, rely=0.0, relheight=1, relwidth=1, anchor="nw")
        
    
    # def on_modified(self):
    #     self.text_box.edit_modified(False)
    #     self.guter.charge_lines()
    #     self.text_box.file_change()
    #     self.tab_frame.change_title_status()

    # def set_tab_frame(self, tab_frame):
    #     self.tab_frame = tab_frame

    # def get_text_box_status(self):
    #     self.text_box.get_text_box_status()
    def show(self):
        self.place(relx=0, rely=0.0, relheight=1, relwidth=1, anchor="nw")

