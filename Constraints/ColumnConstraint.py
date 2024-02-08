from Constraints.Constraint import Constraint
from Entities.Map import Map
from Expressions.Expression import Expression
from State import State


class ColumnConstraint(Constraint):
    def __init__(self, name, expr:Expression):
        super().__init__()
        self.name = name
        self.expr=expr

    def correct(self, state:State):
        col=self.expr.eval(state)
        pos = state.map.position(self.name)
        if pos:
            if pos[1]==col:
                return True
        return False

    def partcorrect(self, state:State):
        col=self.expr.eval(state)
        pos = state.map.position(self.name)
        if pos:
            if pos[1] == col:
                return True
            return False
        return True


