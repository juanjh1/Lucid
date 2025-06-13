
class MainEditorAdapter():
    def __init__(self, main_editor_frame):
        self._main_editor_frame = main_editor_frame

    def create_new_view(self):
        self._main_editor_frame.create_new_view()