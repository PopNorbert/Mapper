from Constraints.Constraint import Constraint
from Entities.Map import Map
from State import State
import operator

class NotConstraint(Constraint):
    def __init__(self, cons: Constraint):
        super().__init__()
        self.cons = cons


    def negated(self):
        return NotConstraint(self.cons.negated())

    def correct(self, state: State):
        return self.cons.negated().correct(state)

    def partcorrect(self, state: State):
        return self.cons.negated().partcorrect(state)

    def __str__(self):
        return f"(NOT {str(self.cons)})"