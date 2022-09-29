hp = 100


def shoot(damage):
    global hp
    hp = damage
    print(f"You dealt damage of {damage}")
    return hp


def fly_left():
    print("You moved left")


def fly_forward():
    print("forward")


def fly_right():
    print("You moved right")


def game_over(name):
    print("Game over "+ name)

if __name__ == '__main__':
        fly_left()
        shoot(15)
        fly_forward()
        fly_right()
        game_over("Artur")
