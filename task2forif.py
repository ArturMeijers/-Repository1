cifri = []
text1 = text.split()

def magic(text):
    for obrabot_text in text:
        if obrabot_text.isalpha():
            cifri = cifri + 1


# bukva = input("Ведите букву которую надо заменить: ")
text1 = input("Ведите текст который надо заменить: ")
print(magic(text1))
print(cifri)