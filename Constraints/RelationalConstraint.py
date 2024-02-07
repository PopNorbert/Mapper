from Constraints.Constraint import Constraint
from Entities.Map import Map


class RelationalConstraint(Constraint):
    def __init__(self, name, line):
        super().__init__()
        self.name = name
        self.line = line

    def correct(self, map: Map):
        pos = map.position(self.name)
        if pos:
            if pos[0] == self.line:
                return True
        return False

    def partcorrect(self, map: Map):
        pos = map.position(self.name)
        if pos:
            if pos[0] == self.line:
                return True
            return False
        return True