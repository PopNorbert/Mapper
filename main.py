from Constraints.LineConstraint import LineConstraint
from Controller import Controller
from Entities.Map import Map

if __name__ == '__main__':
    c = Controller(Map(3, 3), ["A", "B", "C", "D"], [LineConstraint("A", 1), LineConstraint("B", 2)])
