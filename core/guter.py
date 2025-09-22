from gui.guter_component import Gutter
from utils.event import Event


class GutterController():

    def __init__(self, parent):

        self.view = Gutter(parent)
        self.lift()
        self.view.disable_edition()
    # this dont work here, need change to show 
    def pack (self, side, fill, before):
        self.view.pack(side=side, fill=fill, before=before)
    
    def update(self, event: Event):

         if Event.EVENT_TYPES.MODIFIED_TEXT_BOX == event.get_type():
            self.refresh_gutter_lines(event.get_data().get("lines")())

    def lift(self):
        self.view.lift()

    def refresh_gutter_lines(self, lines: int):
        self.view.update_line_numbers(lines)

