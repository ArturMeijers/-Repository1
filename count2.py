user_sentence = input("Uzraksti teikumu: ")
Burtu_skaits = 0
Vardu_skaits = 0
Ciparu_skaits = 0

spisok = user_sentence.split()

for words in spisok:
    if words.isalpha():
        Vardu_skaits = Vardu_skaits + 1


for character in user_sentence:
    if character.isalpha():
        Burtu_skaits = Burtu_skaits + 1

for character in user_sentence:
    if character.isspace():
        Vardu_skaits = Vardu_skaits + 1

for character in user_sentence:
    if character.isnumeric():
        Ciparu_skaits = Ciparu_skaits + 1
print("Ievadītājā teksta ir" ,Vardu_skaits,"vārdi," ,Burtu_skaits ,"būrti", "ciparu skaits", Ciparu_skaits)