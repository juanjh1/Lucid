import customtkinter as ctk
import tkinter as tk 
class Gutter(ctk.CTkTextbox):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#4378a2", corner_radius=0)

    def _run_with_editable (self, callback, *args):
        self.configure(state="normal")
        callback(*args) 
        self.configure(state="disabled")
       
    def disable_edition(self):
        self.configure(state="disabled")

    def get_full_content(self)-> str:
        return self.get("1.0", tk.END)
    
    def insert_at_start(self, value:str ) -> None:
        self.insert("1.0", value)
    
    def insert_at_espesific_row(self,line: int, value: str):
        self.insert(f"{line}.0", value)
    
    def get_lines_of_file(self, current_file)-> int:
          return len(current_file.split("\n")) - 1
    
    def add_lines(self, offset:int, additional_lines)-> None :
        final = [ str(offset + i)+"\n" for i in range(additional_lines)]
        
        self.insert_at_espesific_row(offset, "".join(final))

    def update_line_numbers(self,lines):
        current_file = self.get_full_content()  

        if(len(current_file)<= 1):
            self._run_with_editable(self.insert_at_start, "".join([str(i+1)+"\n" for i in range(lines-1)]) )

        else:

            current_lines = self.get_lines_of_file(current_file)-1 
            addition = lines - current_lines 
            print(f"addtition: {addition} lines_number: {lines} current_lines: {current_lines}") 
            if(addition > 0):
                self._run_with_editable(self.add_lines, current_lines,addition ) 
            else:
                ...
    def show(self, before):
        self.pack(side="left", fill="y", before=before)

