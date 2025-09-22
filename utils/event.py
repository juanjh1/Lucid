from  enums.event import  Event_E

class Event:
    EVENT_TYPES = Event_E
    def __init__(self, type, data:dict={}):
        self.type:Event_E = type
        self.data = data
    def get_type(self) -> Event_E:
        return self.type
    def get_data(self) -> dict:
        return self.data
    
