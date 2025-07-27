from .options_controller import OptionController
from gui.nab_item_button_component import NabItemButton


class  NavItemButtonComponent:

    def __init__(self, parent, root_adapter, text):
        
        self.options = None
        self.root = root_adapter
        self.view = NabItemButton(parent,  text, lambda: self.open_modal())
    

    def pack(self, side):
         
         self.view.pack(side=side)
    
    def open_modal(self):

        if self.options is not None:
            self.destroy_buttons()
            return
        
        self.setup_buttons()

           

    def setup_buttons(self):

            #variables
            x = self.view.winfo_x() + 3.5
            y = self.view.winfo_y() + self.view.winfo_height() + 5
            self.options = self.root.set_frame_in_app(OptionController) 

            #layout
            self.options.place_view(x=x, y=y, relwidth=0.1, anchor="nw")
            self.options.lift()

    def destroy_buttons(self):
            self.options.destroy()
            self.options = None
        
    def get_view(self):
         return self.view