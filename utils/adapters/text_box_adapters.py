
class TextBoxAdapterToScroll:
    def __init__(self, text_box):
        self.text_box = text_box




class TextBoxAdapterToGutter:
    def __init__(self, text_box):
        self._text_box = text_box

    def line_number(self):
        return self.count_textbox_lines()
    
    def get_space_height(self):
        return self.get_space_height()
    