import random

# Функция выбора персонажа и его способности
def choose_character():
    while True:
        character = input("Выберите персонажа (пират или рыбак): ").lower()
        if character == "пират":
            ability = "выпить ягеря"
            break
        elif character == "рыбак":
            ability = "поймать рыбку"
            break
        else:
            print("Некорректный выбор персонажа. Попробуйте снова.")
    return character, ability

# Запрос выбора персонажей у пользователей
player1_character, player1_ability = choose_character()
player2_character, player2_ability = choose_character()

# Запрос размера поля у пользователя
while True:
    try:
        field_size = int(input("Введите размер поля (одно число): "))
        if field_size <= 0:
            print("Размер поля должен быть положительным числом.")
        else:
            break
    except ValueError:
        print("Ошибка ввода. Попробуйте снова.")

# Запрос количества кораблей у пользователя
while True:
    try:
        num_ships = int(input("Введите количество кораблей (одно число): "))
        if num_ships <= 0:
            print("Количество кораблей должно быть положительным числом.")
        elif num_ships > field_size:
            print("Количество кораблей не может быть больше размера поля.")
        else:
            break
    except ValueError:
        print("Ошибка ввода. Попробуйте снова.")

# Создаем пустое поле для каждого игрока
player1_field = [['~' for _ in range(field_size)] for _ in range(field_size)]
player2_field = [['~' for _ in range(field_size)] for _ in range(field_size)]

# Создаем поле для кораблей
ship_field = [['~' for _ in range(field_size)] for _ in range(field_size)]

# Генерируем и размещаем корабли
ships = []
for _ in range(num_ships):
    while True:
        length = random.randint(1, 4)
        is_vertical = random.choice([True, False])

        if is_vertical:
            x = random.randint(0, field_size - 1)
            y = random.randint(0, field_size - length)
            if all(ship_field[y+i][x] == '~' for i in range(length)):
                for i in range(length):
                    ship_field[y+i][x] = 'S'
                ships.append((x, y, is_vertical, length))
                break
        else:
            x = random.randint(0, field_size - length)
            y = random.randint(0, field_size - 1)
            if all(ship_field[y][x+i] == '~' for i in range(length)):
                for i in range(length):
                    ship_field[y][x+i] = 'S'
                ships.append((x, y, is_vertical, length))
                break

# Переменные для отслеживания активации способностей
player1_ability_used = False
player2_ability_used = False

# Функция для показа всех кораблей и завершения игры
def surrender():
    print("Вы сдались! Вот все корабли:")
    for ship in ships:
        x, y, is_vertical, length = ship
        if is_vertical:
            for i in range(length):
                player1_field[y+i][x] = 'S'
                player2_field[y+i][x] = 'S'
        else:
            for i in range(length):
                player1_field[y][x+i] = 'S'
                player2_field[y][x+i] = 'S'

    # Выводим поле с кораблями для каждого игрока
    print("Поле игрока 1:")
    print("   " + ' '.join(str(i) for i in range(field_size)))
    for i, row in enumerate(player1_field):
        print(f"{i}  {' '.join(row)}")

    print("Поле игрока 2:")
    print("   " + ' '.join(str(i) for i in range(field_size)))
    for i, row in enumerate(player2_field):
        print(f"{i}  {' '.join(row)}")

# Игровой цикл
current_player = 1
while True:
    # Определяем текущего игрока и его поле
    if current_player == 1:
        current_field = player1_field
        opponent_field = player2_field
        current_ability_used = player1_ability_used
        current_character = player1_character
        current_ability = player1_ability
    else:
        current_field = player2_field
        opponent_field = player1_field
        current_ability_used = player2_ability_used
        current_character = player2_character
        current_ability = player2_ability

    # Выводим поле текущего игрока с номерами строк
    print(f"Поле игрока {current_player}:")
    print("   " + ' '.join(str(i) for i in range(field_size)))
    for i, row in enumerate(current_field):
        print(f"{i}  {' '.join(row)}")

    # Пользователь вводит координаты выстрела или команду "сдаюсь"
    while True:
        user_input = input("Введите координаты выстрела (X Y) или 'сдаюсь': ")
        if user_input.lower() == 'сдаюсь':
            surrender()
            exit()
        try:
            x, y = map(int, user_input.split())
            if x < 0 or x >= field_size or y < 0 or y >= field_size:
                raise ValueError
            break
        except ValueError:
            print("Неверные координаты. Попробуйте снова.")

    # Проверяем, попал ли текущий игрок в корабль оппонента, и обновляем поля
    if any(ship[0] <= x < ship[0] + ship[3] and ship[1] <= y < ship[1] + ship[3] for ship in ships):
        print("Попадание!")
        current_field[y][x] = 'X'
        if current_ability_used:
            for ship in ships:
                ship_x, ship_y, is_vertical, length = ship
                if ship_x <= x < ship_x + length and ship_y <= y < ship_y + length:
                    if is_vertical:
                        for i in range(length):
                            current_field[ship_y+i][ship_x] = 'X'
                            opponent_field[ship_y+i][ship_x] = 'X'
                    else:
                        for i in range(length):
                            current_field[ship_y][ship_x+i] = 'X'
                            opponent_field[ship_y][ship_x+i] = 'X'
                    print("Корабль полностью уничтожен!")
                    break
    else:
        print("Мимо!")
        current_field[y][x] = 'O'
        opponent_field[y][x] = 'O'

    # Проверяем условие победы
    if all(current_field[y][x] != '~' for y in range(field_size) for x in range(field_size)):
        print(f"Игрок {current_player} победил! Все корабли потоплены!")
        break

    # Активируем способность текущего игрока, если она не была использована
    if not current_ability_used:
        if current_character == "пират":
            pirate_input = input("Активировать способность 'выпить ягеря'? (да/нет): ")
            if pirate_input.lower() == "да":
                current_ability_used = True
                print("Активирована способность пирата!")
        elif current_character == "рыбак":
            fisherman_input = input("Активировать способность 'поймать рыбку'? (да/нет): ")
            if fisherman_input.lower() == "да":
                current_ability_used = True
                print("Активирована способность рыбака!")
                fish_revealed = 0
                while fish_revealed < 5:
                    x = random.randint(0, field_size - 1)
                    y = random.randint(0, field_size - 1)
                    if current_field[y][x] == '~':
                        current_field[y][x] = 'F'
                        opponent_field[y][x] = 'F'
                        fish_revealed += 1

    # Переключаемся на следующего игрока
    current_player = 2 if current_player == 1 else 1
