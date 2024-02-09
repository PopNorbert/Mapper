from Constraints.ColumnConstraint import  ColumnConstraint
from Constraints.LogicConstraint import LogicConstraint
from Constraints.NotConstraint import NotConstraint
from Constraints.RelationalConstraint import RelationalConstraint
from Controller import Controller
from Entities.Map import Map
from Expressions.ColumnExpression import ColumnExpression
from Expressions.LengthExpression import LengthExpression
from Expressions.LineExpression import LineExpression
from Expressions.ValueExpression import ValueExpression
from State import State

if __name__ == '__main__':
    open("log.txt", "w")
    c = Controller(State(Map(3,3), ["A", "B", "C","D"]), [RelationalConstraint(LineExpression("A"), ValueExpression(2), "<"),
                                                          RelationalConstraint(LengthExpression("A","B"), LengthExpression("C","D"), "=="),
                                                          RelationalConstraint(ColumnExpression("A"), ValueExpression(2), "<"),
                                                          RelationalConstraint(LengthExpression("A","B"), ValueExpression(2), "==")])
    if c.allstep():
        print(c.state.map)
