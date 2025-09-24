import tkinter as tk
import tkinter.font as tkFont


class TextBox(tk.Text):
    SPACING = 14
    def __init__(self, parent)-> None:
        #defaults 
        super().__init__(parent, wrap="none")
        
        self.lift()

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
    
    def deactivate_modified(self)-> None:
        self.edit_modified(False)

    def compare_buffers(self, buffer: str) -> bool:
        
        return self.get_all_buffer() == buffer

    def get_line(self)-> int:

        print(f"insertion at {self.index("insert")}")
        
        return int(self.index("insert").split(".")[0])

    def get_font_heigth(self)-> int:
        font = tkFont.Font( font=self.cget("font") )
        line_height = font.metrics( "linespace" )

        return line_height + TextBox.SPACING  

    def show(self) -> None:
         self.pack(side="left", expand=True, fill="both")
