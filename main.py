from Constraints.LogicConstraint import LogicConstraint
from Constraints.NotConstraint import NotConstraint
from Constraints.RelationalConstraint import RelationalConstraint
from Controller import Controller
from Entities.Map import Map
from Expressions.AggregateExpression import AggregateExpression
from Expressions.ColumnExpression import ColumnExpression
from Expressions.LengthExpression import LengthExpression
from Expressions.LineExpression import LineExpression
from Expressions.ValueExpression import ValueExpression
from State import State
import time as t

if __name__ == '__main__':
    open("log.txt", "w")
    c = Controller(State(Map(10,10), {"H":4, "B":7, "K":5}),
                   [

                        NotConstraint(RelationalConstraint(LengthExpression("H","H"), ValueExpression(2), ">")),
                        RelationalConstraint(LengthExpression("B","B"), ValueExpression(1), ">="),
                        RelationalConstraint(ColumnExpression("B"), ValueExpression(8), "=="),
                        RelationalConstraint(LengthExpression("H","B"), ValueExpression(5), ">="),
                        RelationalConstraint(LengthExpression("K","H"), ValueExpression(3), ">=")
                   ])
    for x in c.consList:
        print(x)
    a = t.time()
    if c.allstep():
        print(c.state.map)
    b = t.time()
    print(f"executed in {b - a} seconds")
