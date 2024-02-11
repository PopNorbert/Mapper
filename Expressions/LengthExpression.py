from Expressions.Expression import Expression
from State import State


class LengthExpression(Expression):
    def __init__(self, name1, name2):
        super().__init__()
        self.name1 = name1
        self.name2 = name2

    def eval(self, state: State):
        a=state.map.position(self.name1)
        b=state.map.position(self.name2)
        res=[]
        if a and b:
            for i in a:
                for j in b:
                    if i!=j:
                        res.append((abs(i[0]-j[0])**2+abs(i[1]-j[1])**2)**0.5)
        if res:
            return res
        return None

    def __str__(self):
        return f"{self.name1}{self.name2}"
