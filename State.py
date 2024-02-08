from Entities.Map import Map
from Entities.Node import Node


class State:
    def __init__(self, map:Map, nodes: list[str]):
        self.map=map
        self.nodes=nodes