from typing import override
import customtkinter as ctk
from gui.tab_frame_componet import TabFrame
from utils.subject import Subject
from utils.path import normalize_path
from utils.observer import Observer
from utils.event import Event
from model.user_input_manager import UserInputManger

class TabController(Subject, Observer ):

    def __init__(self, parent, path):
        super().__init__()
        self.view = TabFrame(parent)
        self.path = path;
        self.frame_name = ctk.StringVar(value=path.name + " ")
        self.label = ctk.CTkLabel(self.view, textvariable=self.frame_name)
        self.last_status = False
        self.button = ctk.CTkButton(
                        self.view,
                        text="x", 
                        width=10, 
                        bg_color="red", 
                        height=5,
                        anchor="center", 
                        fg_color="red",
                        command= self.close_curren_file
                        )

        # layout 
        self.label.pack(side="left", padx = 10)
        self.button.pack(side="right", pady = 5, padx = 5)
        
        # #events
        self.label.bind("<Button-1>", self.stacke_frame)
        self.view.bind("<Button-1>", self.stacke_frame)

        
    def stacke_frame(self, _) -> None:
        for observer in self._observers:
            observer.update(Event(Event.EVENT_TYPES.STACK_VIEW))
    
    @override 
    def update(self, event: Event) -> None:
        if Event.EVENT_TYPES.MODIFIED_TEXT_BOX.is_equal(event.get_type()):
            self.change_modified_status(event.get_data().get("status"))

    def change_modified_status(self, status)-> None:
        path = ""
        
        if status and not self.last_status :
              path = " *"
        if not status and self.last_status:
              path = ""

        self.frame_name.set(value=self.path.name + path)
        self.last_status = status
    
    def close_curren_file(self) -> None:
        
        if not self.last_status:
           self._destroy()
           return

        user_input =  UserInputManger.ask_yes_or_no("Lucid", f"Do you want to save the changes do made to {self.path.name} ") 
        
        if not user_input:
            return
        # toca guardar aqui, hagalo mañana porfa
        self._destroy()
         
    
    def _destroy(self)-> None:

        for observer in self._observers:
            observer.update(Event("SELF_DESTRUCTION", {"s_path": normalize_path(self.path)}))           
        
        self.view.destroy()
    
    def pack(self)-> None:
        self.view.pack(side="left",ipadx=20, padx=3)
