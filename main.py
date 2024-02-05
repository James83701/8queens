import random
import copy
from Board import Board

chessBoard = Board([])
chessBoard.printBoard()
# print(chessBoard.queenCoordinates)
# print(chessBoard.H)

stateChanges = 0
restarts = 0

def findNextState(nextB):
    global stateChanges
    global restarts
    global chessBoard
    neighborWithLowerH = 0
    nextBoard = None
    for i in nextB:
        if i.H < chessBoard.H:
            neighborWithLowerH += 1
            nextBoard = copy.deepcopy(i)
    if neighborWithLowerH == 0:
        print("Neighbors found with lower h: 0")
        print("RESTART")
        chessBoard = Board([])
        restarts += 1
    else:
        print(f"Neighbors found with lower h: {neighborWithLowerH}")
        print("Setting new current state")
        chessBoard = copy.deepcopy(nextBoard)
        chessBoard.copyinit()
        stateChanges += 1


##final output

while chessBoard.H != 0:
    print("")
    print(f"Current h: {chessBoard.H}")
    print("Current State")
    chessBoard.printBoard()
    nextB = chessBoard.generateNextListOfBoards()
    findNextState(nextB)
print("Current State")
chessBoard.printBoard()
print("Solution Found!")
print(f"State changes: {stateChanges}")
print(f"Restarts: {restarts}")


