import operator

from Constraints.Constraint import Constraint
from Entities.Map import Map
from State import State


class LogicConstraint(Constraint):
    def __init__(self, cons1:Constraint, cons2:Constraint, operation):
        super().__init__()
        self.cons1=cons1
        self.cons2=cons2
        self.op = operation
        self.operators = {
            "&&":operator.and_,
            "||":operator.or_
        }
        self.neg = {
            "&&":"||",
            "||":"&&"
        }
    def negated(self):
        return LogicConstraint(self.cons1.negated(),self.cons2.negated(), self.neg[self.op])


    def correct(self, state:State):
        return self.operators[self.op](self.cons1.correct(state),self.cons2.correct(state))


    def partcorrect(self,  state:State):
        return self.operators[self.op](self.cons1.partcorrect(state), self.cons2.partcorrect(state))

    def __str__(self):
        return f"({str(self.cons1)} {self.op} {str(self.cons2)})"