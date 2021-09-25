
class Player:
    def __init__(self, name):
        self.name = name
        self.id = self.findID()
        self.plays = False
        self.racePieces = []
    def findID(self):
        self.id = 'X'
        if self.name == 'p1':
            return self.id
        elif self.name == 'p2':
            self.id = 'O'
            return self.id