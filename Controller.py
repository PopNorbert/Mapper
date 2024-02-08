from State import State


class Controller:
    def __init__(self, state: State, consList):
        self.state = state
        self.nodes = self.state.nodes
        self.consList = consList
        self.currcons = []

    def allpartcorrect(self):
        for x in self.currcons:
            if not x.partcorrect(self.state):
                return False
        return True

    def log(self, nodes, map, i, j):
        with open("log.txt", "a") as f:
            f.write(f"\n{i} {j}\n{nodes}\n{map}\n")

    def allcorrect(self):
        for x in self.currcons:
            if not x.correct(self.state):
                return False
        return True

    def onestep(self):
        if self.consList:
            self.currcons.append(self.consList[0])
        if self.backtrack(0, 0, self.nodes[:]):
            return True
        return False

    def allstep(self):
        self.currcons = self.consList
        if self.backtrack(0, 0, self.nodes[:]):
            return True
        return False

    def backtrack(self, i, j, nodenames):
        map = self.state.map
        for name in nodenames:
            map[i][j].name = name
            self.log(nodenames, map, i, j)
            if self.allpartcorrect():
                if self.allcorrect() and len(nodenames) == 1:
                    return True
                newn = nodenames[:]
                newn.remove(name)
                if j==map.width-1 and i!=map.height-1:
                    if self.backtrack(i+1,0,newn):
                        return True
                if j!=map.width-1:
                    if self.backtrack(i,j+1,newn):
                        return True
        map[i][j].name = "."
        if j == map.width - 1 and i != map.height - 1:
            if self.backtrack(i + 1, 0, nodenames[:]):
                return True
        if j!= map.width - 1:
            if self.backtrack(i, j + 1, nodenames[:]):
                return True
        return False

