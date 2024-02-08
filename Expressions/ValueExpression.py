from Expressions.Expression import Expression
from State import State


class ValueExpression(Expression):
    def __init__(self, value):
        super().__init__()
        self.value=value

    def eval(self, state:State):
        return self.value

