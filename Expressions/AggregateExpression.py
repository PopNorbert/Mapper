from math import floor

from Expressions.Expression import Expression
from State import State


class AggregateExpression(Expression):
    def __init__(self, ex:Expression, op):
        super().__init__()
        self.ex=ex
        self.op=op

    def eval(self, state:State):
        c = self.ex.eval(state)
        if not c:
            return None
        if len(c) == 1:
            return c[0]
        match self.op:
            case "min":
                return [min(c)]
            case "max":
                return [max(c)]
            case "avg":
                return [floor(sum(c)/len(c))]
    def __str__(self):
        return f"{self.op}({str(self.ex)})"

