

from .tab_container_controller import TabMainFrameController
from .text_container_controller import TextMainFrameController
from gui.editor_frame import MainFrame
from model.user_input_manager import UserInputManger
from pathlib import Path
from utils.adapters.main_frame_adapter import MainEditorAdapter


class MainEditorFrameController:
    
    def __init__(self, parent):
        self.view = MainFrame(parent)
        self.tab = TabMainFrameController(self.view)
        self.tab.place(relx=0, rely=0, relheight=0.05, relwidth=1, anchor="nw")
        self.textframe = TextMainFrameController(self.view)
        self.tabs = {}


    def get_main_editor_adapter(self):
        return MainEditorAdapter(self)
    
    def find_tab(self, path):
        """
        The path should be a absolute string path
        """
        print(self.tabs.get(path))
        print(self.tab)
        return self.tabs.get(path)
    def set_new_tab(self, path, tab):
        if tab is None:
            raise RuntimeError("The tab can't be None")
        if self.find_tab(path) is None:
            self.tabs[path] = tab
            tab.pack()
        else:
            print("stak please")
            return None
        return tab
        
    def create_new_view(self):
        path = UserInputManger.select_file()
        file_selected = Path(path)
        tab_item = self.set_new_tab(path, self.tab.create_tab(file_selected))
        if tab_item is None: #need refactor 
            return None
        text_item = self.textframe.create_new_view(file_selected)
        tab_item.add_observer(text_item)
        text_item.add_observer(tab_item)

    
    def place(self, relx, rely, relheight, relwidth, anchor):
        self.view.place(
                        relx=relx, 
                        rely=rely, 
                        relheight=relheight, 
                        relwidth=relwidth, 
                        anchor=anchor)

