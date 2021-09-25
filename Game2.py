

from Dice import Dice
from Square import Square
from Board import Board
from Piece import Piece
from Player import Player

class Game2:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.createPlayers()
    def create(self, A, player):
        for i in range(A[1]):
            piece = Piece()
            piece.playerOwner = player
            self.board.squares[A[0]].pieces.append(piece)
    def createPlayers(self):
        self.thesis1 = [23, 15]
        self.thesis2 = [11, 15]
        self.create(self.thesis1, self.player1)
        self.create(self.thesis2, self.player2)
    
    def __str__(self):
        return '             >>> '+self.player1.name+' VS '+self.player2.name+' <<< '+'\n'+str(self.board)
    