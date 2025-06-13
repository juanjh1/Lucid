class Event:
    def __init__(self, type, data=None):
        self.type = type
        self.data = data
    def get_type(self):
        return self.type
    def get_data(self):
        return self.data
    
