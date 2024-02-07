class Controller:
    def __init__(self, map, nodes, consList):
        self.map = map
        self.consList = consList
        self.nodes=nodes

    def onestep(self):
        constraint = self.consList[0]
        self.consList = self.consList[1:]
