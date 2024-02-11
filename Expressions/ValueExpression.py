from Expressions.Expression import Expression
from State import State


class ValueExpression(Expression):
    def __init__(self, value):
        super().__init__()
        if isinstance(value,list):
            self.value=value
        else:
            self.value=[value]

    def eval(self, state:State):
        return self.value

    def __str__(self):
        return ', '.join(str(i) for i in self.value)

