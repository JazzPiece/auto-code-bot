def check_guess(board, x, y):
    if board[x][y] == 'S':
        board[x][y] = 'X'
        return True
    else:
        board[x][y] = '*'
        return False

filename: check_win.py
code:
def check_win(board):
    for row in board:
        if 'S' in row:
            return False
    return True

filename: player_guess.py
code:
def player_guess():
    x = int(input("Enter the x coordinate: "))
    y = int(input("Enter the y coordinate: "))
    return x, y