from dataclasses import dataclass

from Entities.Node import Node


@dataclass
class Map:
    height: int
    width: int

    def __post_init__(self):
        self.data = [[Node(iposition=i, jposition=j) for i in range(self.width)] for j in range(self.height)]
