import random

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

# Создаем пустое поле для пользователя
user_field = [['~' for _ in range(field_size)] for _ in range(field_size)]

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

# Функция для показа всех кораблей и завершения игры
def surrender():
    print("Вы сдались! Вот все корабли:")
    for ship in ships:
        x, y, is_vertical, length = ship
        if is_vertical:
            for i in range(length):
                user_field[y+i][x] = 'S'
        else:
            for i in range(length):
                user_field[y][x+i] = 'S'

    # Выводим поле с кораблями
    print("   " + ' '.join(str(i) for i in range(field_size)))
    for i, row in enumerate(user_field):
        print(f"{i}  {' '.join(row)}")

# Игровой цикл
while True:
    # Выводим поле пользователя с номерами строк
    print("   " + ' '.join(str(i) for i in range(field_size)))
    for i, row in enumerate(user_field):
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

    # Проверяем, попал ли пользователь в корабль, и обновляем поле пользователя
    if any(ship[0] <= x < ship[0] + ship[3] and ship[1] <= y < ship[1] + ship[3] for ship in ships):
        print("Попадание!")
        user_field[y][x] = 'X'
    else:
        print("Мимо!")
        user_field[y][x] = 'O'

    # Проверяем условие победы
    if all(user_field[y][x] != '~' for y in range(field_size) for x in range(field_size)):
        print("Поздравляем! Вы потопили все корабли!")
        break
