
from gui.scroll_frame_component import ScrollContainer
class ScrollController:
    def __init__(self, parent, text_box_adapter):
        self.view = ScrollContainer(parent, text_box_adapter)
        self.text_box_adapter = text_box_adapter
        self.parent_heigth = parent.winfo_height()
        self.last_move  = None
        self.text_box_heigth = self.text_box_adapter.get_total_heigth()
        
    

             # events
        self.text_box_adapter.bind("<Configure>", lambda e: self.configure_size_of_scroll_bar())
        parent.bind("<Configure>", lambda e: self.configure_size_of_scroll_bar())

        self.bind("<Button-1>", lambda e: print(e))
        self.scroll.bind("<B1-Motion>", lambda e: self.calculate_move(e))

        self.after(100, self.configure_size_of_scroll_bar)
        self.pack(side="left", fill="y" )

    def configure_size_of_scroll_bar(self):
            # variables
            text_box_size = self.text_box.get_total_heigth()
            view_height = self.master.winfo_height()
            scroll_height = self.winfo_height() 

            if (text_box_size < view_height):
                if self.scroll.winfo_ismapped():
                    self.scroll.pack_forget()
                return
                
            height = (view_height / text_box_size) * scroll_height
            self.scroll.configure(height=height)
            self.scroll.pack()

    def calculate_move(self, event):
        event_y = event.y
        if  self.last_move is None:
            self.last_move = event_y
        y = self.scroll.winfo_y()

        fraction = (event_y - y) /  self.winfo_height()
        fraction = min(1.0, max(0.0, fraction))
        print(fraction)
        self.master.yview_moveto(fraction)

           
class ScrollContainer(ctk.CTkFrame):
    def __init__(self, parent, text_box):
        #defaults 
        super().__init__(parent, fg_color="gray", corner_radius=0, width= ScrollBar.SCROLL_BAR_WIDTH) 
        self.scroll= ScrollBar(self)

        #variables      
        self.text_box =text_box
        self.parent_heigth = parent.winfo_height()
        self.last_move  = None
        self.text_box_heigth = self.text_box.get_total_heigth()
        self.after(100, self.configure_size_of_scroll_bar)


   



    def configure_size_of_scroll_bar(self):
        # variables
        text_box_size = self.text_box.get_total_heigth()
        view_height = self.master.winfo_height()
        scroll_height = self.winfo_height() 

        if (text_box_size < view_height):
            if self.scroll.winfo_ismapped():
                self.scroll.pack_forget()
            return
            
        height = (view_height / text_box_size) * scroll_height
        self.scroll.configure(height=height)
        self.scroll.pack()

    def calculate_move(self, event):
        event_y = event.y
        if  self.last_move is None:
            self.last_move = event_y
        y = self.scroll.winfo_y()

        fraction = (event_y - y) /  self.winfo_height()
        fraction = min(1.0, max(0.0, fraction))
        print(fraction)
        self.master.yview_moveto(fraction)