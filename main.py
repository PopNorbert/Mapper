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
    c = Controller(State(Map(3,3), ["A", "B", "C","D"]), [RelationalConstraint(LengthExpression("A","B"), LengthExpression("C","D"), ">"),
                                                          RelationalConstraint(ColumnExpression("A"), ValueExpression(0),"=="),
                                                          RelationalConstraint(LineExpression("A"), ValueExpression(1),"=="),
                                                          RelationalConstraint(ColumnExpression("C"), ValueExpression(1),"=="),
                                                          RelationalConstraint(LineExpression("C"), ValueExpression(1),"=="),
                                                          RelationalConstraint(LineExpression("D"), ValueExpression(1),"=="),
                                                          RelationalConstraint(ColumnExpression("D"), ValueExpression(2),"==")])
    if c.allstep():
        print(c.state.map)
