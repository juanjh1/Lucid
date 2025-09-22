from utils.path import normalize_path
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
        return self.tabs.get(path)

    def set_new_tab(self, path, tab):
        
        if tab is None:
            raise RuntimeError("The tab can't be None")

        if self.find_tab(path) is None:
            self.tabs[normalize_path(path)] = tab
            tab.pack()
        else:
            print("stak please")
            return None

        return tab

    def update(self, event):
        if event.get_type() == "SELF_DESTRUCTION":
            self.del_tab(event.data.get("s_path"))

    def del_tab(self, name):
        print("entre")

        print(self.tabs)
        del self.tabs[name]

    def create_new_view(self):
        path = UserInputManger.select_file()
        file_selected = Path(path)
        tab_item = self.set_new_tab(file_selected, self.tab.create_tab(file_selected))
        
        if tab_item is None: #need refactor 
            assert  RuntimeError("you ")

        text_item = self.textframe.create_new_view(file_selected)
        tab_item.add_observer(text_item)
        text_item.add_observer(tab_item)
        tab_item.add_observer(self)

    
    def place(self, relx, rely, relheight, relwidth, anchor):
        self.view.place(
                        relx=relx, 
                        rely=rely, 
                        relheight=relheight, 
                        relwidth=relwidth, 
                        anchor=anchor)

