from enum import Enum

class Event_E(Enum):

    MODIFIED_TEXT_BOX ="MODIFIED_TEXT_BOX"
    STACK_VIEW = "STACK_VIEW"
    SELF_DESTRUCTION ="SELF_DESTRUCTION"

    def is_equal(self, instance)-> bool:
        return instance == self
