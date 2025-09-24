from utils.event import Event
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
        
        self.text_box = TextBoxController(self.view, path)
        self.guter = GutterController(self.view)

        self.text_box.add_observer(self)
        self.text_box.add_observer(self.guter)

        self.text_box.show()
        self.guter.show(before=self.text_box.get_view())
        
        self.show()
        self.lift()

    def lift(self):
        self.view.lift()
    
    def show(self):
        self.view.show()

    def tab_adapter(self):
        return ViewAdapterToTab(self)
    
    def update(self, event:Event):

        if Event.EVENT_TYPES.STACK_VIEW.is_equal(event.get_type()):
            self.lift()
        if Event.EVENT_TYPES.MODIFIED_TEXT_BOX.is_equal(event.get_type()):
            self.text_box_update(event)
        if Event.EVENT_TYPES.SELF_DESTRUCTION.is_equal(event.get_type()):
            self._destroy()
    
    def text_box_update(self, event):
        
        for observer in self._observers:
            observer.update(event)
    
    def _destroy(self):
        self.view.destroy()

