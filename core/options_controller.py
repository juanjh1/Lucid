from gui.option_frame_componet import OptionFrame
#from utils.dialog_utils import create_frame

class OptionController:
    def __init__(self, root):
        self.root = root
        self.buttons = self.get_buttons()
        self.view = OptionFrame(root, self.buttons)

    def get_buttons(self):
        return {
            "Open": lambda: self.root.create_view()
              }

    def place_view(self, x, y, relwidth, anchor):
        self.view.place(x=x, y=y, relwidth=relwidth, anchor=anchor)
    
    def lift(self):
        self.view.lift()

    def destroy(self):
        self.view.destroy()