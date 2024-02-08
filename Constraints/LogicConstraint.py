from Constraints.Constraint import Constraint
from Entities.Map import Map
from State import State


class LogicConstraint(Constraint):
    def __init__(self, cons1:Constraint, cons2:Constraint, operation):
        super().__init__()
        self.cons1=cons1
        self.cons2=cons2
        self.op = operation

    def correct(self, state:State):
        match self.op:
            case "and":
                return self.cons1.correct(state) and self.cons2.correct(state)
            case "or":
                return self.cons1.correct(state) or self.cons2.correct(state)


    def partcorrect(self,  state:State):
        match self.op:
            case "and":
                return self.cons1.partcorrect(state) and self.cons2.partcorrect(state)
            case "or":
                return self.cons1.partcorrect(state) or self.cons2.partcorrect(state)