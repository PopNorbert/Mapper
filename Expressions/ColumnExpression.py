from Entities.Node import Node
from Expressions.Expression import Expression
from State import State


class ColumnExpression(Expression):
    def __init__(self, name):
        super().__init__()
        self.name=name

    def eval(self, state:State):
        if state.map.position(self.name):
            return state.map.position(self.name)[1]
        return None
