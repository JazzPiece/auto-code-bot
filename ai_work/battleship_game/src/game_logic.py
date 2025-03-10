def check_guess(board, x, y):
    if board[x][y] == 'S':
        board[x][y] = 'X'
        return True
    else:
        board[x][y] = '*'
        return False

def check_win(board):
    for row in board:
        if 'S' in row:
            return False
    return True