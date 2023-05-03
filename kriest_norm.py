import random

#spisok
matrica = {'1': ' ', '2': ' ', '3': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '7': ' ', '8': ' ', '9': ' '}
board_keys = []
for key in matrica:
    board_keys.append(key)
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
def botMove():
    possible_moves = [key for key in matrica if matrica[key] == ' ']
    if possible_moves:
        move = random.choice(possible_moves)
        matrica[move] = 'O'
        return True
    else:
        return False
def game():
    cross = 'X'
    count = 0
    gameOver = False
    for i in range(9):
        printBoard(matrica)
        if cross == 'X':
            print("Введите куда поставить X: ")
            move = input()
            if matrica[move] == ' ':
                matrica[move] = cross
                count += 1
            else:
                print("Это место уже заполнено:( Переместить в другое место ?")
                continue
        else:
            print('щас робот ходит')
            botMoved = botMove()
            if botMoved:
                count += 1
        if count >= 5:
            if matrica['7'] == matrica['8'] == matrica['9'] != ' ':
                gameOver = True
            elif matrica['4'] == matrica['5'] == matrica['6'] != ' ':
                gameOver = True
            elif matrica['1'] == matrica['2'] == matrica['3'] != ' ':
                gameOver = True
            elif matrica['1'] == matrica['4'] == matrica['7'] != ' ':
                gameOver = True
            elif matrica['2'] == matrica['5'] == matrica['8'] != ' ':
                gameOver = True
            elif matrica['3'] == matrica['6'] == matrica['9'] != ' ':
                gameOver = True
            elif matrica['7'] == matrica['5'] == matrica['3'] != ' ':
                gameOver = True
            elif matrica['1'] == matrica['5'] == matrica['9'] != ' ':
                gameOver = True
            if gameOver:
                printBoard(matrica)
                print("Игра окончена.")
                if cross == 'X':
                    print(" **** Ура, ты выиграл ****")
                else:
                    print(" **** Блин,ты проиграл ****")
                break
        if count == 9:
            printBoard(matrica)
            print("Игра окончена")
            break
        if cross == 'X':
            cross = 'O'
        else:
            cross = 'X'
    restart = input("Еще каточку? (y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            matrica[key] = " "
        game()
if __name__ == "__main__":
    game()