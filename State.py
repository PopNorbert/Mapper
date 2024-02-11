from Entities.Map import Map
from Entities.Node import Node


class State:
    def __init__(self, map:Map, nodes: dict[str:int]):
        self.map=map
        self.nodes=nodes