import random
class Board:
    # done up to counting heuristics
    boardList = []
    def __init__(self, boardList):
        self.boardList = boardList
        if boardList == []:
            self.resetBoard()
    
    def resetBoard(self):
        self.boardList = [[0 for i in range(8)] for j in range(8)]
        
        for column in range(8):
            self.boardList[column][random.randint(0, 7)] = 1

    def printBoard(self):
        for row in range(8):
            for column in range(8):
                print(self.boardList[column][row], end = '')
                if column != 7:
                    print(", ", end = '')
            print("")

    def moveQueen(self, column, newRow):
        for row in range(8):
            self.boardList[column][row] = 0
        self.boardList[column][newRow] = 1  

    def checkRow(self, column, row):
        conflict = set()
        for checkColumn in range(8):
            if (self.boardList[checkColumn][row] == 1) and column != checkColumn:
                conflict.add(tuple([checkColumn, row]))
                conflict.add(tuple([column, row]))
                
        return conflict

    def countH(self):
        queensInConflict = set()
        for row in range(8):
            for column in range(8):
                if self.boardList[column][row] == 1:
                    queensInConflict = queensInConflict.union(self.checkRow(column, row))
                    queensInConflict = queensInConflict.union(self.checkDiagonal(column, row))
        
        return queensInConflict

    def checkDiagonal(self, column, row):
        conflict = set()
        conflict = conflict.union(self.checkDiagonalNorthEast(column, row))
        conflict = conflict.union(self.checkDiagonalNorthWest(column, row))
        conflict = conflict.union(self.checkDiagonalSouthEast(column, row))
        conflict = conflict.union(self.checkDiagonalSouthWest(column, row))
        return conflict
    
    def checkDiagonalNorthEast(self, column, row):
        conflict = set()
        for i in range(1, 8):
            
            if column + i < 8 and row + i < 8:
                if (self.boardList[column + i][row + i] == 1):
                    conflict.add(tuple([column, row]))
            else:
                break

        return conflict
    
    def checkDiagonalNorthWest(self, column, row): # col -, row +
        conflict = set()
        for i in range(1, 8):
            if column - i > -1 and row + i < 8:
                if (self.boardList[column - i][row + i] == 1):
                    conflict.add(tuple([column, row]))
            else:
                break
        return conflict
    
    def checkDiagonalSouthEast(self, column, row):# col +, row -
        conflict = set()
        for i in range(1, 8):
            if column + i < 8 and row - i > -1:
                if (self.boardList[column + i][row - i] == 1):
                    conflict.add(tuple([column, row]))
            else:
                break
        return conflict
    
    def checkDiagonalSouthWest(self, column, row):# col -, row -
        conflict = set()
        for i in range(1, 8):
            
            if column - i > -1 and row - i > -1:
                if (self.boardList[column - i][row - i] == 1):
                    conflict.add(tuple([column, row]))
            else:
                break
        return conflict
    
    def generateNextBoardList(self):
        permutationBoard = Board(self.boardList)
        nextBoardList = []

        for row in range(8):
            for column in range(8):
                if permutationBoard.boardList[column][row] == 1:
                    for i in range(7, 0, -1):
                        if i == row:
                            continue
                        
                        nextBoardList.append((Board((permutationBoard.moveQueen(column, i)).boardList)))
        return nextBoardList
    
    def setBoardList(self, boardList):
        self.boardList = boardList

    def testPrintBoards(self, nextBoardList):
        for Board in nextBoardList:
            Board.printBoard()




    
