import customtkinter as ctk
from gui.tab_frame_componet import TabFrame
from utils.subject import Subject
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
        self.button = ctk.CTkButton(self.view, text="x", 
                                    width=10, bg_color="red", 
                                    height=5,
                                    anchor="center", 
                                    fg_color="red",
                                    command= self.close_curren_file)

        # layout 
        self.label.pack(side="left", padx = 10)
        self.button.pack(side="right", pady = 5, padx = 5)
        self.view.pack(side="left",ipadx=20, padx=3)
        # #events
        self.label.bind("<Button-1>", self.stacke_frame)
        self.view.bind("<Button-1>", self.stacke_frame)

        
    def stacke_frame(self, event):
        for observer in self._observers:
                observer.update(Event("STACK_VIEW", None))
    def update(self, event):
        if event.get_type() == "MODIFIED_TEXT_BOX":
            self.change_modified_status(event.get_data().get_status())

    def change_modified_status(self, status):
         
         if status and not self.last_status :
              self.frame_name.set(value=self.path.name + " *")
         if not status and self.last_status:
              self.frame_name.set(value=self.path.name + " ")
            
         #else:
              #self.frame_name.set(value=self.path.name)
         self.last_status = status
    def close_curren_file(self):
        if not self.last_status:
           self._destroy()
           return

        user_input =  UserInputManger.ask_yes_or_no("Lucid", f"Do you want to save the changes do made to {self.path.name} ") 
        
        if not user_input:
            return
        # toca guardafd aqui hagalo mañana porfa
        self._destroy()
         
    
    def _destroy(self):
           for observer in self._observers:
                  observer.update(Event("SELF_DESTRUCTION", None))
           self.view.destroy()