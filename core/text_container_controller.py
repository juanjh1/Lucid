
from gui.text_editor_container_component import TextFrame
from .view_controller import ViewController
class TextMainFrameController:
    def __init__(self, parent):
        self.view = TextFrame(parent)
    def pack(self, relx, rely , relheight , relwidth, anchor):
        self.place(relx=relx, 
                   rely=rely, 
                   relheight=relheight, 
                   relwidth=relwidth, 
                   anchor=anchor)

    def create_new_view(self, path):
        return ViewController(self.view, path)
    
