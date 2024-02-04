import random
from Board import Board


chessBoard = Board([])
chessBoard.printBoard()
print(len(chessBoard.countH()))
nextBoardList = chessBoard.generateNextBoardList()
chessBoard.testPrintBoards(nextBoardList)
print



