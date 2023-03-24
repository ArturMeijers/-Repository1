string = input("Enter string or numbers: ")
char_count = {}
for char in string:
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1
# Этот цикл перебирает каждый символ во входной строке. Для каждого символа он проверяет, является ли символ уже ключом в словаре char_count. Если нет, он добавляет символ в
# качестве ключа в словарь со значением 1. Если символ уже является ключом в словаре, он увеличивает значение, связанное с этим ключом, на 1.
# К концу этого цикла char_count будет содержать количество каждого символа во входной строке.
for key, value in char_count.items():
    print(key + "-" + str(value))

