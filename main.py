import random
from Board import Board
from HeuristicChecking import HeuristicChecking

chessBoard = Board([])
chessBoard.printBoard()
print(chessBoard.queenCoordinates)


nextB = chessBoard.generateNextListOfBoards()
x=10
while x>0:
    for i in nextB:
        i.printBoard()
        print(i.queenCoordinates)
        print("////////////////")
        x = x-1


