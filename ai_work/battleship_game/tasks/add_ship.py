def add_ship(board, ship_size):
    size = len(board)
    while True:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            x = random.randint(0, size - 1)
            y = random.randint(0, size - ship_size)
            if all(board[x][y+i] == 'O' for i in range(ship_size)):
                for i in range(ship_size):
                    board[x][y + i] = 'S'
                break
        else:
            x = random.randint(0, size - ship_size)
            y = random.randint(0, size - 1)
            if all(board[x+i][y] == 'O' for i in range(ship_size)):
                for i in range(ship_size):
                    board[x + i][y] = 'S'
                break
    return board

filename: print_board.py
code:
def print_board(board):
    for row in board:
        print(' '.join(row))

filename: play_battleship.py
code:
size = 10
board = create_board(size)
board = add_ship(board, 3)
board = add_ship(board, 4)

while not check_win(board):
    print_board(board)
    guess = input("Enter your guess in format 'x y': ")
    x, y = map(int, guess.split())
    if check_guess(board, x, y):
        print("Hit!")
    else:
        print("Miss!")

print("You sank all the ships! Game over.")