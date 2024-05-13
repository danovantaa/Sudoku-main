def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)

    return None

def is_valid(board, number, position):
    for i in range(len(board)):
        if board[position[0]][i] == number and position[1] != i:
            return False
        if board[i][position[1]] == number and position[0] != i:
            return False

    x = position[0] // 3
    y = position[1] // 3
    for i in range(x*3, x*3 + 3):
        for j in range(y*3, y*3 +3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True

def solve(board):
    empty = find_empty(board)

    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def result(board):
    if solve(board):
        return board