import random
def freshBoard():
    board = []
    for j in range(8):
        row = []

        for i in range(8):
            row.append(0)

        board.append(row)
    for i in range(8):
        board[random.randint(0, 7)][i] = 1
    return board

def printBoard(board):
    for x in range(rows):
        for y in range(columns):
            print(board[x][y], end = '')
            if y != 7:
                print(", ", end = '')
        print()

def moveQueen(board, column, newRow):
    for i in range(8):
        board[i][column] = 0
    board[newRow][column] = 1
    return board


rows = 8
columns = 8
chessBoard = freshBoard()
printBoard(chessBoard)




