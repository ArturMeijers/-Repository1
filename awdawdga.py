import random

# Initialize board with numbers
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print board function
def print_board():
    for row in board:
        print("|".join(str(cell) for cell in row))
        # print("|".join(row))


# Get user move function
def get_user_move():
    while True:
        move = int(input("Enter a number from 1 to 9 to place your X: "))
        row = (move - 1) // 3
        col = (move - 1) % 3
        if 1 <= move <= 9:
            if board[row][col] == move:
                board[row][col] = "X"
                break
            else:
                print("That cell is already occupied. Try again.")
        else:
            print("Invalid input. Try again.")

# Get bot move function
def get_bot_move():
    while True:
        move = random.randint(1, 9)
        row = (move - 1) // 3
        col = (move - 1) % 3
        if board[row][col] == move:
            board[row][col] = "O"
            break

# Check winner function
def check_winner():
    # Check rows
    for row in board:
        if row.count("X") == 3:
            return "X"
        elif row.count("O") == 3:
            return "O"

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "-":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]

    # Check for tie
    if all(isinstance(cell, str) for row in board for cell in row):
        return "TIE"

    # Game is still ongoing
    return None

# Main game loop
while True:
    print_board()

    # Get user move
    get_user_move()

    # Check for winner or tie
    winner = check_winner()
    if winner:
        print_board()
        if winner == "TIE":
            print("It's a tie!")
        else:
            print(f"{winner} wins!")
        break

    # Get bot move
    get_bot_move()

    # Check for winner or tie
    winner = check_winner()
    if winner:
        print_board()
        if winner == "TIE":
            print("It's a tie!")
        else:
            print(f"{winner} wins!")
        break
