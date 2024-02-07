class Controller:
    def __init__(self, map, nodenames, consList):
        self.map = map
        self.consList = consList
        self.nodenames = nodenames
        self.currcons = []

    def allpartcorrect(self):
        for x in self.currcons:
            if not x.partcorrect(self.map):
                return False
        return True

    def allcorrect(self):
        for x in self.currcons:
            if not x.correct(self.map):
                return False
        return True

    def onestep(self):
        if self.consList:
            self.currcons.append(self.consList[0])
        if self.backtrack(0, 0, self.nodenames[:]):
            return True
        return False

    def allstep(self):
        self.currcons = self.consList
        if self.backtrack(0, 0, self.nodenames[:]):
            return True
        return False
    def backtrack(self, i, j, nodenames):
        if self.allcorrect() and nodenames == []:
            return True
        for name in nodenames:
            self.map[i][j].name = name
            if self.allpartcorrect():
                c = nodenames.index(name)
                nodenames.remove(name)
                if j == self.map.width - 1:
                    if i != self.map.height - 1:
                        if self.backtrack(i + 1, 0, nodenames):
                            return True
                else:
                    if self.backtrack(i, j + 1, nodenames):
                        return True
                nodenames.insert(c, name)
            else:
                self.map[i][j].name="."
                if j == self.map.width - 1:
                    if i != self.map.height - 1:
                        if self.backtrack(i + 1, 0, nodenames):
                            return True
                else:
                    if self.backtrack(i, j + 1, nodenames):
                        return True

        return False
