import random

def create_board(size):
    board = [['O' for _ in range(size)] for _ in range(size)]
    return board

def place_ship(board, ship_size):
    direction = random.choice(['horizontal', 'vertical'])
    size = len(board)
    if direction == 'horizontal':
        x = random.randint(0, size - 1)
        y = random.randint(0, size - ship_size)
        for i in range(ship_size):
            board[x][y + i] = 'S'
    else:
        x = random.randint(0, size - ship_size)
        y = random.randint(0, size - 1)
        for i in range(ship_size):
            board[x + i][y] = 'S'
    return board

size = 10
board = create_board(size)
board = place_ship(board, 3)
board = place_ship(board, 4)

for row in board:
    print(row)