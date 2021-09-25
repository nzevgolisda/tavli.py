
from Dice import Dice
from Square import Square
from Board import Board
from Piece import Piece
from Player import Player

class Game:
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
        self.thesis1 = [0, 15]
        self.thesis2 = [23, 15]
        self.create(self.thesis1, self.player1)
        self.create(self.thesis2, self.player2)
    def determineFirst(self, player1, player2):
        while [player1.plays, player2.plays] == [False, False]:
            if self.board.dice[0].value != self.board.dice[1].value:
                break
            else:
                self = Game(player1, player2)
        a = self.board.dice[0].value
        b = self.board.dice[1].value
        if a < b:
            player2.plays = True
        elif a > b:
            player1.plays = True
        ##
        for player in [player1, player2]:
            if player.plays == True:
                player.throw = [self.board.dice[0].value, self.board.dice[1].value]
                print('Player ',player.name,' plays first.')
                print('First throw for ',player.name,' is ',player.throw)
            else:
                continue
    def determineSecond(self, player1, player2):
        self = Game(player1, player2)
        for player in [player1, player2]:
            if player.plays == False:
                player.throw = [self.board.dice[0].value, self.board.dice[1].value]
                print('Player ',player.name,' plays second.')
                print('First throw for ',player.name,' is ',player.throw)
            else:
                continue
    
    def __str__(self):
        return '             >>> '+self.player1.name+' VS '+self.player2.name+' <<< '+'\n'+str(self.board)