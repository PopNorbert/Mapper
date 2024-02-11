from abc import ABC

from Entities.Map import Map
from State import State


class Constraint(ABC):
    def __init__(self):
        pass

    def correct(self, state:State):
        pass

    def partcorrect(self,state:State):
        pass

    def negated(self):
        pass

    def __str__(self):
        pass