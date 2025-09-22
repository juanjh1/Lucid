import tkinter as tk

class TextBox(tk.Text):
    SPACING = 14
    def __init__(self, parent)-> None:
        #defaults 
        super().__init__(parent, wrap="none")
        self.lift()

        #configure
        #self.tag_add("espaciado", "1.0", "end")
        #self.tag_configure("espaciado", spacing3=TextBox.SPACING)
        #layout
        self.pack( side="left", expand=True, fill="both")
    
    def register_events(self, config_dict: dict)-> None:

        for (name, callback) in config_dict.items():
           self.bind(name, callback) 
    
    def insert_file_at_start(self, content: str)-> None:

        self.insert("1.0", content)

    def get_all_buffer(self)-> str:
        return self.get("1.0", tk.END)

    def buffer_lines(self)-> int:
        return  len(self.get_all_buffer().split("\n"))
    
    def compare_buffers(self, buffer: str) -> bool:
        return self.get_all_buffer() == buffer
