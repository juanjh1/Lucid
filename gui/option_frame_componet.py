
import customtkinter as ctk

class OptionFrame(ctk.CTkFrame):
    def __init__(self, parent, buttons: dict[str, callable]):
        super().__init__(parent, fg_color="white", corner_radius=0)
        self.load_buttons(buttons)

    def load_buttons(self, buttons):
        for text, callback in buttons.items():
            button = ctk.CTkButton(self, text=text, compound="left", corner_radius=0, anchor="w")
            button.configure(command=callback)
            button.pack(expand=True, fill="x")
