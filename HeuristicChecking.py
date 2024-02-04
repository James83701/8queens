

def countH(self) -> set:
    queensInConflict = set()
    for queen in self.queenCoordinates:
        queensInConflict = queensInConflict.union(self.checkRow(column, row))
        queensInConflict = queensInConflict.union(self.checkDiagonal(column, row))
    
    return queensInConflict

def checkRow(board: Board, column: int, row: int) -> set:
    conflict = set()
    for checkColumn in range(8):
        if (board.boardList[checkColumn][row] == 1) and column != checkColumn:
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