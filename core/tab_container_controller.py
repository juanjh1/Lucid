
from gui.tab_container_component import TabMainFrame
from .tab_controller import TabController

class TabMainFrameController:
    def __init__(self, parent):
        self.view = TabMainFrame(parent)
    def pack(self, relx, rely , relheight , relwidth, anchor):
        self.view.place(
                   relx=relx, 
                   rely=rely, 
                   relheight=relheight, 
                   relwidth=relwidth, 
                   anchor=anchor
                   )
    def create_tab(self, file):
        return TabController(self.view, file)

    