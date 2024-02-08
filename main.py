from Constraints.ColumnConstraint import ColumnConstraint
from Constraints.LineConstraint import LineConstraint
from Constraints.LogicConstraint import LogicConstraint
from Constraints.NotConstraint import NotConstraint
from Controller import Controller
from Entities.Map import Map
from Expressions.ColumnExpression import ColumnExpression
from Expressions.LineExpression import LineExpression
from Expressions.ValueExpression import ValueExpression
from State import State

if __name__ == '__main__':
    open("log.txt", "w")
    c = Controller(State(Map(3,3), ["A", "B", "C","D"]), [ColumnConstraint("C", ColumnExpression("A")),LineConstraint("A", ValueExpression(1)), LineConstraint("B", ValueExpression(2)), ColumnConstraint("A", ValueExpression(1)), LineConstraint("C", ValueExpression(2))])
    if c.allstep():
        print(c.state.map)
