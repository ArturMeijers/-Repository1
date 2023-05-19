import random

class Pirate:
    def __init__(self):
        self.ability_available = True

    def use_ability(self, ships, x, y):
        self.ability_available = False
        for ship in ships:
            if ship[0] <= x < ship[0] + ship[3] and ship[1] <= y < ship[1] + ship[3]:
                ships.remove(ship)
                return True
        return False

    def is_ability_available(self):
        return self.ability_available

class Fisherman:
    def __init__(self):
        self.ability_available = True

    def use_ability(self, user_field):
        self.ability_available = False
        num_revealed = 0
        while num_revealed < 5:
            x = random.randint(0, len(user_field[0]) - 1)
            y = random.randint(0, len(user_field) - 1)
            if user_field[y][x] == '~':
                user_field[y][x] = '?'
                num_revealed += 1

    def is_ability_available(self):
        return self.ability_available

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

# Выбор персонажа
print("Выберите персонажа:")
print("1. Пират (может выпить ягеря и потопить задетый корабль)")
print("2. Рыбак (может поймать рыбку и открыть 5 неизвестных мест)")
character_choice = input("Введите номер персонажа: ")

if character_choice == '1':
    character = Pirate()
elif character_choice == '2':
    character = Fisherman()
else:
    print("Неверный выбор персонажа. Будет выбран персонаж по умолчанию.")
    character = Pirate()

# Создаем пустое поле для пользователя
user_field = [['~' for _ in range(field_size)] for _ in range(field_size)]

# Создаем поле для кораблей
ship_field = [['~' for _ in range(field_size)] for _ in range(field_size)]

# Генерируем и размещаем корабли
ships = []
for _ in range(num_ships):
    while True:
        x = random.randint(0, field_size - 1)
        y = random.randint(0, field_size - 1)
        is_vertical = random.choice([True, False])
        length = random.randint(1, 4)
        if is_vertical:
            if y + length <= field_size and all(ship_field[y + i][x] == '~' for i in range(length)):
                for i in range(length):
                    ship_field[y + i][x] = 'S'
                ships.append((x, y, is_vertical, length))
                break
        else:
            if x + length <= field_size and all(ship_field[y][x + i] == '~' for i in range(length)):
                for i in range(length):
                    ship_field[y][x + i] = 'S'
                ships.append((x, y, is_vertical, length))
                break

# Функция активации способности персонажа
def activate_ability():
    if isinstance(character, Pirate):
        if character.use_ability(ships, x, y):
            user_field[y][x] = 'S'
            print("Персонаж потопил корабль!")
    elif isinstance(character, Fisherman):
        character.use_ability(user_field)

# Игровой цикл
while True:
    # Выводим поле пользователя с номерами строк
    print("   " + ' '.join(str(i) for i in range(field_size)))
    for i, row in enumerate(user_field):
        print(f"{i}  {' '.join(row)}")

    # Пользователь вводит координаты выстрела или команду "сдаюсь" или активирует способность
    while True:
        user_input = input("Введите координату X или команду 'сдаюсь' или 'способность': ")
        if user_input.lower() == 'сдаюсь':
            for ship in ships:
                x, y, _, _ = ship
                user_field[y][x] = 'S'
            print("Вы сдались. Все корабли:")
            for row in user_field:
                print(' '.join(row))
            exit()
        elif user_input.lower() == 'способность':
            if character.is_ability_available():
                activate_ability()
                print("Вы активировали способность!")
                break
            else:
                print("Способность уже была использована. Введите координату X.")
        else:
            try:
                x = int(user_input)
                y = int(input("Введите координату Y: "))
                if x < 0 or x >= field_size or y < 0 or y >= field_size:
                    raise ValueError
                break
            except ValueError:
                print("Неверные координаты. Попробуйте снова.")

    # Проверяем, попал ли пользователь в корабль, и обновляем поле пользователя
    if any(ship[0] <= x < ship[0] + ship[3] and ship[1] <= y < ship[1] + ship[3] for ship in ships):
        print("Попадание!")
        if isinstance(character, Pirate):
            activate_ability()
            print("Персонаж выполнил способность!")
        else:
            for ship in ships:
                if ship[0] <= x < ship[0] + ship[3] and ship[1] <= y < ship[1] + ship[3]:
                    user_field[ship[1]:ship[1] + ship[3]][ship[0]] = ['S'] * ship[3]
                    print("Корабль уничтожен!")
                    break
    else:
        print("Промах!")
        user_field[y][x] = 'O'

    # Проверяем, остались ли еще корабли на поле
    if not ships:
        print("Поздравляем! Вы потопили все корабли!")
        exit()
