from gui.text_box_components import TextBox
from model.file_model import FileManager
from utils.subject import Subject
from utils.event import Event


class TextBoxController(Subject):

    def __init__(self, parent, path):
        super().__init__()
        self.text_box = TextBox(parent)
        self.last_index = 0
        self.file_content = self.load_file_content(path)
        

        self.highlight_line()
        self.insert_file_content()
        self.text_box.tag_configure("resaltado", background="#ffeaa7")  
        self.status = False

        event_config = {
            "<KeyRelease>": self.highlight_line,
            "<ButtonRelease-1>": self.highlight_line,
            "<<Modified>>": self.on_modified
        }
       
        self.text_box.register_events(event_config)
    
    def show(self):
        self.text_box.show()

    def insert_file_content(self) -> None:
  
        if self.file_content is None:
            raise RuntimeError("File is not loaded")

        self.text_box.insert_file_at_start(self.file_content)

    
    def load_file_content(self, path) -> str:

        return FileManager.open_file(path)
    
    def file_change(self)-> None:

        self.status = self.text_box.compare_buffers(self.file_content)

    def get_total_height(self)-> int:

        return self.get_space_heigth() * self.textbox_lines()
    
    #tab methods
    def get_status(self):

        return self.status
    
    def on_modified(self, _)-> None:

        self.text_box.deactivate_modified()
        self.file_change()

        for observer in self._observers:
            observer.update(Event(
                            Event.EVENT_TYPES.MODIFIED_TEXT_BOX, 
                            {
                            "lines":self.textbox_lines,
                            "status": self.status
                            }
                            ))

    def textbox_lines(self)-> int:

        return  self.text_box.buffer_lines()

    def get_space_heigth(self) -> int :

        return self.text_box.get_font_heigth() 

    def get_view(self):

        return self.text_box
    
    def highlight_line(self, _=None) -> None:

        line = self.text_box.get_line()

        if self.last_index != line:
            self.text_box.tag_remove("resaltado", f"{self.last_index}.0", f"{self.last_index}.end")
              
        self.text_box.tag_add("resaltado", f"{line}.0", f"{line}.end")
        self.last_index = line
  
