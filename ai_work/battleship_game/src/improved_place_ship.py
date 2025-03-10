def place_ship(board, ship_size):
    direction = random.choice(['horizontal', 'vertical'])
    size = len(board)
    if direction == 'horizontal':
        x = random.randint(0, size - 1)
        y = random.randint(0, size - ship_size)
        for i in range(ship_size):
            if board[x][y + i] == 'S':
                return place_ship(board, ship_size)
            board[x][y + i] = 'S'
    else:
        x = random.randint(0, size - ship_size)
        y = random.randint(0, size - 1)
        for i in range(ship_size):
            if board[x + i][y] == 'S':
                return place_ship(board, ship_size)
            board[x + i][y] = 'S'
    return board