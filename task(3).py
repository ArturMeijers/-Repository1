def replace_at_indices(text, indices, symbol):
    new_text = ''
    for i in range(len(text)):
        if i in indices:
            new_text += symbol
        else:
            new_text += text[i]
    return new_text


text = input("Вводите звездочки: ")
a = int(input("Введите первый индекс: "))
b = int(input("Введите второй индекс: "))
c = int(input("Введите третий индекс: "))
indices = [a, b, c]
symbol = input("Введите букву: ")

new_text = replace_at_indices(text, indices, symbol)
print(new_text)

# indices_str = input("Вводите индекси как на примере - (e.g., 1,3,6): ")
# indices = [int(i) for i in indices_str.split(',')]


