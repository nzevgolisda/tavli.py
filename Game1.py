
from Dice import Dice
from Square import Square
from Board import Board
from Piece import Piece
from Player import Player

class Game1:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.createPlayers()
    def create(self, A, B, player):
        k = 0
        for j in A:
            for i in range(B[k]):
                piece = Piece()
                piece.playerOwner = player
                self.board.squares[j].pieces.append(piece)
            k += 1
    def createPlayers(self):
        self.thesis1 = [5, 7, 12, 23]
        self.thesis2 = [0, 11, 16, 18]
        self.quantity1 = [5, 3, 5, 2]
        self.quantity2 = [2, 5, 3, 5]
        self.create(self.thesis1, self.quantity1, self.player1)
        self.create(self.thesis2, self.quantity2, self.player2)
    
    def __str__(self):
        return '             >>> '+self.player1.name+' VS '+self.player2.name+' <<< '+'\n'+str(self.board)
    