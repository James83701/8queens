def chessBoardInit():
    board = []
    for j in range(8):
        row = []

        for i in range(8):
            row.append(0)

        board.append(row)

    return board

rows = 8
columns = 8
chessBoard = chessBoardInit()


def printBoard(chessBoard):
    for x in range(rows):
        for y in range(columns):
            print(chessBoard[x][y], end = '')
            if y != 7:
                print(", ", end = '')
        print()

printBoard(chessBoard)