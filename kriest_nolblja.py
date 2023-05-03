import random

board = [' ' for _ in range(9)]

def print_board():
    row1 = '|'.join(board[0:3])
    row2 = '|'.join(board[3:6])
    row3 = '|'.join(board[6:9])
    print(row1)
    print('-----')
    print(row2)
    print('-----')
    print(row3)

def player_move():
    while True:
        move = input("Введите номер ячейки для своего хода (от 1 до 9): ")
        try:
            move = int(move) - 1
            if move >= 0 and move <= 8:
                if board[move] == ' ':
                    board[move] = 'X'
                    return
                else:
                    print("Эта ячейка уже занята. Попробуйте другую.")
            else:
                print("Введите число от 1 до 9.")
        except ValueError:
            print("Введите число от 1 до 9.")

def computer_move():
    free_cells = [i for i, cell in enumerate(board) if cell == ' ']
    if free_cells:
        move = random.choice(free_cells)
        board[move] = 'O'

def check_win(player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    return False

def main():
    print("Добро пожаловать в игру Крестики-нолики!")
    print_board()
    while True:
        player_move()
        print_board()
        if check_win('X'):
            print("Вы победили!")
            break
        computer_move()
        print_board()
        if check_win('O'):
            print("Компьютер победил.")
            break
        if ' ' not in board:
            print("Ничья.")
            break

if __name__ == '__main__':
    main()
