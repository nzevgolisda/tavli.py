
from Dice import Dice
from Square import Square
from Piece import Piece

class Board:
    def __init__(self):
        self.racePieces = []
        self.capturedPieces = []
        self.dice = [Dice(), Dice()]
        self.createSquares()
    def createSquares(self):
        self.squares = []
        for i in range(24):
            self.squares.append(Square(i))
    def flip(self):
        squares_copy = self.squares
        for i in range(23, -1, -1):
            square_copy = squares_copy[i]
            self.squares[i] = square_copy


    def __str__(self):
        s = ''
        for sq in self.squares:
            s += str(sq)+'\n'
        return s
    
