class Piece:
    def __init__(self):
        self.playerOwner = None
    def __str__(self):
        return '('+self.playerOwner.id+')'