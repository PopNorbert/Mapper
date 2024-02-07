from abc import ABC

from Entities.Map import Map


class Constraint(ABC):
    def __init__(self):
        pass

    def correct(self, map:Map):
        pass

    def partcorrect(self,map:Map):
        pass