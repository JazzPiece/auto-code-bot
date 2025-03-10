def player_guess(size):
    while True:
        try:
            x = int(input("Enter the x coordinate (0-{}): ".format(size-1))
            y = int(input("Enter the y coordinate (0-{}): ".format(size-1))
            if 0 <= x < size and 0 <= y < size:
                return x, y
            else:
                print("Coordinates out of range. Try again.")
        except ValueError:
            print("Invalid input. Please enter integers.")