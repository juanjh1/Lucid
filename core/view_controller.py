import tkinter as tk
from.text_box_controler import TextBoxController
from gui.view_component import TextFrame
from utils.adapters.view_adapter import ViewAdapterToTab
from utils.observer import Observer
from utils.subject import Subject
from .guter import GutterController


class ViewController(Observer, Subject):
    def __init__(self, parent, path):
        super().__init__()
        self.view = TextFrame(parent)
        #canvas_manager
        # self.canvas = tk.Canvas(parent, background="red")
        # self.canvas.pack(expand=True, fill="both", )
        

        
        #components
        
        self.text_box = TextBoxController(self.view, path)
        self.guter = GutterController(self.view)

        # self.canvas.create_window((0,0), window=self.view, anchor="nw", width=parent.winfo_width())

        #self.canvas.configure(scrollregion=(0,0,  parent.winfo_width() ,self.text_box.get_total_heigth()))
        
    
        ##self.scroll = ScrollContainer(self.canvas, self.text_box)
        #self.tab_frame = None



        ## add_observers
        self.text_box.add_observer(self)
        self.text_box.add_observer(self.guter)

        #layout sone
        self.text_box.pack("left", True, "both")
        self.guter.pack(side="left", fill="y", before=self.text_box.get_view())
        self.view.place(relx=0, rely=0.0, relheight=1, relwidth=1, anchor="nw")
        # self.canvas.place(relx=0, rely=0.0, relheight=1, relwidth=1, anchor="nw")

        #lift 
        self.view.lift()



    def lift(self):
        self.view.lift()

    def tab_adapter(self):
        return ViewAdapterToTab(self)
    

    def update(self, event):
        if event.get_type() == "STACK_VIEW":
            self.lift()
        if event.get_type() == "MODIFIED_TEXT_BOX":
            self.text_box_update(event)
        if event.get_type() == "SELF_DESTRUCTION":
            self._destroy()
    def notify_observers(self):
        pass


    def text_box_update(self, event):
        for observer in self._observers:
            observer.update(event)
    def _destroy(self):
        self.view.destroy()


    # def on_modified(self):
    #     self.text_box.edit_modified(False)
    #     self.guter.charge_lines()
    #     self.text_box.file_change()
    #     self.tab_frame.change_title_status()

    #def set_tab_frame(self, tab_frame):
    #     self.tab_frame = tab_frame

    # def get_text_box_status(self):
    #     self.text_box.get_text_box_status()
    