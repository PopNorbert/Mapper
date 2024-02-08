from abc import ABC

from State import State


class Expression(ABC):
    def __init__(self):
        pass

    def eval(self, state:State):
        pass
