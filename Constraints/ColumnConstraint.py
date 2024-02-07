from Constraints.Constraint import Constraint
from Entities.Map import Map


class ColumnConstraint(Constraint):
    def __init__(self, name, col):
        super().__init__()
        self.name = name
        self.col = col

    def correct(self, map: Map):
        pos = map.position(self.name)
        if pos:
            if pos[1]==self.col:
                return True
        return False

    def partcorrect(self, map:Map):
        pos = map.position(self.name)
        if pos:
            if pos[1] == self.col:
                return True
            return False
        return True


