

class AppAdapeterToFileOption():
    def __init__(self, app):
        self._app = app

    def set_frame_in_app(self, object ):
        return self._app.set_frame_in_main_app(object)
