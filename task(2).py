
text = input("Введите текст: ")
letter = input("Введите букву: ")
start = text.find(letter)
ramocki = []
while start != -1:
    ramocki.append(start)
    start = text.find(letter, start + 1)
print(ramocki)

