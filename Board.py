import random
import copy

class Board:
    boardList = []
    queenCoordinates = []
    queensInConflict = set()
    H = 999
    def __init__(self, boardList: list):
        self.boardList = boardList
        if boardList == []:
            self.resetBoard()
        self.getQueens()
        self.countH()
    
    def copyinit(self):
        self.queensInConflict = set()
        self.getQueens()
        self.countH()

    def resetBoard(self) -> None:
        self.boardList = [[0 for i in range(8)] for j in range(8)]
        
        for column in range(8):
            self.boardList[column][random.randint(0, 7)] = 1
    
    def getQueens(self) -> None:
        self.queenCoordinates = []
        for column in range(8):
            for row in range(8):
                if self.boardList[column][row] == 1:
                    self.queenCoordinates.append([column, row])

    def printBoard(self) -> None:
        for row in range(8):
            for column in range(8):
                print(self.boardList[column][row], end = '')
                if column != 7:
                    print(", ", end = '')
            print("")

    def moveQueen(self, column: int, newRow: int) -> None:
        for row in range(8):
            self.boardList[column][row] = 0
        self.boardList[column][newRow] = 1  
        self.getQueens()


    
    def generateNextListOfBoards(self):
        
        nextListOfBoards = []
        for queen in self.queenCoordinates:
            permutationBoard = copy.deepcopy(self)
            for rowChange in range(7, 0, -1):
                if queen[1] == rowChange:
                    continue
                else:
                    permutationBoard.moveQueen(queen[0], rowChange)
                    permutationBoard.copyinit()
                    nextListOfBoards.append(copy.deepcopy(permutationBoard))
        return nextListOfBoards
        # for row in range(8):
        #     for column in range(8):
        #         if permutationBoard.boardList[column][row] == 1:
        #             for i in range(7, 0, -1):
        #                 if i == row:
        #                     continue
                        
        #                 nextBoardList.append((Board((permutationBoard.moveQueen(column, i)).boardList)))
        # return nextBoardList
    
    def setBoardList(self, boardList):
        self.boardList = boardList

    def testPrintBoards(self, nextBoardList):
        for Board in nextBoardList:
            Board.printBoard()


####################
    def countH(self):
        for queen in self.queenCoordinates:
            self.queensInConflict = self.queensInConflict.union(self.checkRow(queen[0], queen[1]))
            self.queensInConflict = self.queensInConflict.union(self.checkDiagonal(queen[0], queen[1]))
        self.H = len(self.queensInConflict)


    def checkRow(self, column: int, row: int) -> set:
        conflict = set()
        for checkColumn in range(8):
            if (self.boardList[checkColumn][row] == 1) and column != checkColumn:
                conflict.add(tuple([checkColumn, row]))
                conflict.add(tuple([column, row]))
                
        return conflict



    def checkDiagonal(self, column: int, row: int) -> set:
        conflict = set()
        conflict = conflict.union(self.checkDiagonalNorthEast(column, row))
        conflict = conflict.union(self.checkDiagonalNorthWest(column, row))
        conflict = conflict.union(self.checkDiagonalSouthEast(column, row))
        conflict = conflict.union(self.checkDiagonalSouthWest(column, row))
        return conflict

    def checkDiagonalNorthEast(self, column: int, row: int) -> set:
        conflict = set()
        for i in range(1, 8):
            
            if column + i < 8 and row + i < 8:
                if (self.boardList[column + i][row + i] == 1):
                    conflict.add(tuple([column, row]))
            else:
                break

        return conflict

    def checkDiagonalNorthWest(self, column: int, row: int) -> set: # col -, row +
        conflict = set()
        for i in range(1, 8):
            if column - i > -1 and row + i < 8:
                if (self.boardList[column - i][row + i] == 1):
                    conflict.add(tuple([column, row]))
            else:
                break
        return conflict

    def checkDiagonalSouthEast(self, column: int, row: int) -> set:# col +, row -
        conflict = set()
        for i in range(1, 8):
            if column + i < 8 and row - i > -1:
                if (self.boardList[column + i][row - i] == 1):
                    conflict.add(tuple([column, row]))
            else:
                break
        return conflict

    def checkDiagonalSouthWest(self, column: int, row: int) -> set:# col -, row -
        conflict = set()
        for i in range(1, 8):
            
            if column - i > -1 and row - i > -1:
                if (self.boardList[column - i][row - i] == 1):
                    conflict.add(tuple([column, row]))
            else:
                break
        return conflict