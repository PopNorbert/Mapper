from dataclasses import dataclass

from Entities.Node import Node


@dataclass
class Map:
    height: int
    width: int

    def __post_init__(self):
        self.data = [[Node(iposition=i, jposition=j) for i in range(self.width)] for j in range(self.height)]

    def __str__(self):
        str = ""
        for row in self.data:
            for n in row:
                str += n.name + " "
            str += "\n"
        return str

    def __getitem__(self, i):
        return self.data[i]

    def position(self, name):
        for i in range(self.height):
            for j in range(self.width):
                if self.data[i][j].name == name:
                    return i, j
        return None
