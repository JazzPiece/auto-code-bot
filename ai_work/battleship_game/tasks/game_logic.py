def play_game():
    size = 10
    board = create_board(size)
    board = place_ship(board, 3)
    board = place_ship(board, 4)
    
    while not check_win(board):
        display_board(board)
        x, y = player_guess()
        if check_guess(board, x, y):
            print("Hit!")
        else:
            print("Miss!")
    
    print("Congratulations! You sank all the ships.")