from Constraints.Constraint import Constraint
from Entities.Map import Map
from State import State


class NotConstraint(Constraint):
    def __init__(self, cons: Constraint):
        super().__init__()
        self.cons = cons

    def correct(self, state: State):
        return not self.cons.correct(state)

    def partcorrect(self, state: State):
        if self.cons.correct(state):
            return False
        return True
