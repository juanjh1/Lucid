import tkinter.font as tkFont
from gui.text_box_components import TextBox
from model.file_model import FileManager
from utils.subject import Subject
from utils.event import Event
class TextBoxController(Subject):
    def __init__(self, parent, path):
        super().__init__()
        self.text_box = TextBox(parent)
        self.file_content = self.load_file_content(path)
        self.last_index = 0
        self.get_actual_line()

        self.insert_file_content("0.0")

        # tags configure
        self.text_box.tag_configure("resaltado", background="#ffeaa7")  
        self.text_box.tag_add("espaciado", "0.0", "end")
        self.text_box.tag_configure("espaciado", spacing3=TextBox.SPACING)
        self.status = False
       

        ##events
        self.text_box.bind("<KeyRelease>", self.get_actual_line)
        self.text_box.bind("<ButtonRelease-1>", self.get_actual_line)
        self.text_box.bind("<<Modified>>", self.notify_observers)
    
    def pack(self, side, expand, fill):
        self.text_box.pack(side=side, expand=expand, fill=fill, pady=4)

    
    def insert_file_content(self, start):
        if self.file_content is None:
            raise RuntimeError("put error")
        self.text_box.insert(start, self.file_content)

    
    def load_file_content(self, path):
        return FileManager.open_file(path)
    
    def file_change(self):
        if self.file_content != self.text_box.get("1.0", "end-1c"):
            self.status = True
            return
        self.status = False

    def get_total_heigth(self):
        return self.text_box.get_space_height() * self.text_box.count_textbox_lines()
    
    #tab methods
    def get_status(self):
        return self.status
    
    #event methods
    def on_modified(self, function_list):
          pass
   
    def notify_observers(self, event):
        self.text_box.edit_modified(False)
        self.file_change()
        for observer in self._observers:
            observer.update(Event("MODIFIED_TEXT_BOX", self))

    ## guter methods 
    def count_textbox_lines(self):
        return  len(self.text_box.get("0.0", "end-1c").split("\n"))
    
            
    def get_space_height(self):
        font = tkFont.Font(font=self.text_box.cget("font"))
        line_height = font.metrics("linespace")
        return line_height + TextBox.SPACING  

    def get_view(self):
        return self.text_box
    def get_actual_line(self, event=None):
         line = self.text_box.index("insert").split(".")[0]
         if self.last_index != line:
            self.text_box.tag_remove("resaltado", f"{self.last_index}.0", f"{self.last_index}.end+1c")   
         self.text_box.tag_add("resaltado", f"{line}.0", f"{line}.end+1c")
         self.last_index = line