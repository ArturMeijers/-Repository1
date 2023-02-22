text = input('Введите текст: ')
letter = input('Введите букву, которую хотите найти: ')

numbers = []
start = 0

while True:
    sub_string = text[start:]
    index = sub_string.find(letter)
    if index == -1:
        break
    numbers.append(start + index)
    start = start + index + 1

print(numbers)
