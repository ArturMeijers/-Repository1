text = input("Введите текст: ")
letter = input("Введите букву: ")
modified_text = text.replace(letter, '*').replace('*', letter, -1)
print(modified_text)



