
from Dice import Dice
from Square import Square
from Board import Board
from Player import Player
from Game import Game

import time
from datetime import datetime
#from Game1 import Game1
#from Game2 import Game2
player1 = Player('p1')
player2 = Player('p2')
game0 = Game(player1, player2)
#game0 = Game1(player1, player2)
#game0 = Game2(player1, player2)
print(game0)

game0.determineFirst(player1, player2)
game0.determineSecond(player1, player2)

print(player1.plays)
print(player2.plays)

## Timer
def timer(moveTime):
    dt = 0
    sec = []
    start = datetime.now()
    print(start)
    while float(dt) < float(moveTime):
        timeStr = str(datetime.now() - start)
        dt = timeStr[5:]
        second = float(dt)
        if second - second//1 < 1/10:
            if second//1 not in sec and int(second//1) in range(1, moveTime+1):
                sec.append(int(second//1))
                print(sec[len(sec)-1])
    print(datetime.now())
timer(3)

# callback
#def runtime(dt = 0.5, a = lambda dt: 2 * dt):
#    return a
#runtimeTest = runtime(dt = 0.5)
#print(runtimeTest)

#print(double(5))

#timer(2.5)

# Runtime example
#now = time.time()
#cdMax = 1
#cd = cdMax
#while(True):
#    now_new = time.time()
#    dt = now_new - now
#    now = now_new
#    cd -= dt
#    if (cd < 0):
#        cd += cdMax
#        print('tick ' + str(cd))
#    #print(dt)
#    time.sleep(0.005)


def runtime(dt, callback):
    #print (time.time())
    n = 1
    print("Secs: " + str(dt))
    callback(dt, n)
print("\n\n\n")

def callback(dt, n):
    print(datetime.now())
    print("DT: " + str(dt))

runtime(0.0166, callback) # 60 fps
