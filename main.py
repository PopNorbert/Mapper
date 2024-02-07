from Constraints.ColumnConstraint import ColumnConstraint
from Constraints.LineConstraint import LineConstraint
from Controller import Controller
from Entities.Map import Map

if __name__ == '__main__':
    c = Controller(Map(3, 3), ["A", "B","C","D"], [ColumnConstraint("A", 0), ColumnConstraint("B", 2), LineConstraint("B",1), LineConstraint("C",1), LineConstraint("A",1)])
    if c.allstep():
        print(c.map)