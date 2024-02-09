from Expressions.Expression import Expression
from State import State


class LengthExpression(Expression):
    def __init__(self, name1, name2):
        super().__init__()
        self.name1 = name1
        self.name2 = name2

    def eval(self, state: State):
        map = state.map
        if map.position(self.name1) and map.position(self.name2):
            return (abs(map.position(self.name1)[0] - map.position(self.name2)[0]) ** 2 + abs(
                map.position(self.name1)[1] - map.position(self.name2)[1]) ** 2) ** 0.5
        return None
