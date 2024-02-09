from Constraints.Constraint import Constraint
from Entities.Map import Map
from Expressions.Expression import Expression
from State import State
import operator


class RelationalConstraint(Constraint):
    def __init__(self, expr1: Expression, expr2: Expression, op):
        super().__init__()
        self.ex1 = expr1
        self.ex2 = expr2
        self.op = op
        self.operators = {
            "==": operator.eq,
            ">=": operator.ge,
            "<=": operator.le,
            "<": operator.lt,
            ">": operator.gt,
            "!=": operator.ne
        }

    def correct(self, state: State):
        if self.ex1.eval(state) is None or self.ex2.eval(state) is None:
            return False
        return self.operators[self.op](self.ex1.eval(state), self.ex2.eval(state))

    def partcorrect(self, state: State):
        if self.ex1.eval(state) is None or self.ex2.eval(state) is None:
            return True
        return self.operators[self.op](self.ex1.eval(state), self.ex2.eval(state))
