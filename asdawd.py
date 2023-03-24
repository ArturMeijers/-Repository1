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

def replace_at_indices(text, indices, symbol):
    new_text = ''
    for i in range(len(text)):
        if i in indices:
            new_text += symbol
        else:
            new_text += text[i]
    return new_text

def replace(string):
    result = ""
    for char in string:
        if char == " ":
            result += " "
        else:
            result += "*"
    return result


text = input('Введите текст: ')
string = text
print(string)
hidden_text = replace(string)
print(hidden_text)

while '*' in hidden_text:
    letter = input('Введите букву, которую хотите найти: ')
    numbers = find_letter_positions(text, letter)
    if not numbers:
        print('Вы ввели неправильную букву, попробуйте еще раз.')
        continue
    replacement_symbol = letter
    hidden_text = replace_at_indices(hidden_text, numbers, replacement_symbol)
    print(hidden_text)

print('Слово раскрыто:', hidden_text)

