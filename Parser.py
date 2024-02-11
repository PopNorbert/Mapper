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
import re
class Parser:
    def __init__(self):
        pass
    def parse(self, file):
        with open(file) as f:
            l = f.readlines()
            c = l[0].strip("()\n").split(",")
            m = Map(int(c[0]),int(c[1]))
            c = l[1].strip("()\n").split(",")
            d={}
            for a in c:
                a = a.split(":")
                d.update({a[0]:int(a[1])})
            s = State(m,d)
            c = []
            for line in f.readlines()[2:]:
                c.append(self.getCons(line))
        return s,c
    def getCons(self, segm):
        a = segm.strip("()\n").split()
        if "NOT" in
