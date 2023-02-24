def find_letter_positions(text, letter):
    numbers = []
    start = 0
    while True:
        sub_string = text[start:]
        index = sub_string.find(letter)
        if index == -1:
            break
        numbers.append(start + index)
        start = start + index + 1
    return numbers


text = input('Введите текст: ')

letter = input('Введите букву, которую хотите найти: ')
numbers = find_letter_positions(text, letter)
print(numbers)
