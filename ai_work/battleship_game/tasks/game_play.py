from game_setup import create_board, place_ship
from game_logic import check_guess, check_win

size = 10
board = create_board(size)
board = place_ship(board, 3)
board = place_ship(board, 4)

while True:
    x = int(input("Enter the x coordinate: "))
    y = int(input("Enter the y coordinate: "))

    if x < 0 or x >= size or y < 0 or y >= size:
        print("Invalid input. Please try again.")
        continue

    if check_guess(board, x, y):
        print("Hit!")
    else:
        print("Miss!")

    if check_win(board):
        print("Congratulations! You sunk all the battleships.")
        break