from Entities.Node import Node
from Expressions.Expression import Expression
from State import State


class ColumnExpression(Expression):
    def __init__(self, name):
        super().__init__()
        self.name=name

    def eval(self, state:State):
        c = state.map.position(self.name)
        if c:
            return [pos[1] for pos in c]
        return None

    def __str__(self):
        return f"C_{self.name}"
