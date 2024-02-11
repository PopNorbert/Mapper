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
        self.neg = {
            "==": "!=",
            "!=": "==",
            ">=": "<",
            ">": "<=",
            "<=": ">",
            "<": ">="
        }

    def negated(self):
        return RelationalConstraint(self.ex1,self.ex2,self.neg[self.op])
    def correct(self, state: State):
        a = self.ex1.eval(state)
        b = self.ex2.eval(state)
        if a is None or b is None:
            return False
        if len(b) != 1:
            raise Exception
        b = b[0]
        for item in a:
            if not self.operators[self.op](item, b):
                return False
        return True

    def partcorrect(self, state: State):
        a=self.ex1.eval(state)
        b=self.ex2.eval(state)
        if a is None or b is None:
            return True
        if len(b) != 1:
            raise Exception
        b = b[0]
        for item in a:
            if not self.operators[self.op](item,b):
                return False
        return True

    def __str__(self):
        return f"({str(self.ex1)} {self.op} {str(self.ex2)})"


