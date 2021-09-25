
from Piece import Piece
class Square:
    def __init__(self, pos):
        self.pos = pos
        self.pieces = []
    def __str__(self):
        s = ''
        for piece in self.pieces:
            s += str(piece)
        return s
s = Square(0)