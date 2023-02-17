text = input("Введите текст: ")
indices = [1, 3, 6]
letter = input("Введите букву: ")


for i in indices:
    text = text[:i] + letter + text[i+1:]

print(text)



