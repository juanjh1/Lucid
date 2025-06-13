import tkinter as tk

class TextBox(tk.Text):
    SPACING = 14
    def __init__(self, parent):
        #defaults 
        super().__init__(parent, wrap="none")
        self.lift()

        #configure
        #self.tag_add("espaciado", "1.0", "end")
        #self.tag_configure("espaciado", spacing3=TextBox.SPACING)
        #layout
        self.pack( side="left", expand=True, fill="both")

