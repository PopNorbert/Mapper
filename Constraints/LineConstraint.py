from Constraints.Constraint import Constraint


class LineConstraint(Constraint):
    def __init__(self, name, line):
        super().__init__()
        self.name = name
        self.line = line
