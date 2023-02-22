def replace_at_indices(text, indices, symbol):
    new_text = ''
    for i in range(len(text)):
        if i in indices:
            new_text += symbol
        else:
            new_text += text[i]
    return new_text


# Izveidojam vārdu, kas jāmin
word = input("Ievadiet vārdu: ")

# Aizstājam 50% no burtiem ar zvaigznēm
num_stars = len(word) // 2
stars_indices = [0] * num_stars
for i in range(num_stars):
    index = int(input(f"Ievadiet {i + 1}. zvaigznītes indeksu (0 - {len(word) - 1}): "))
    stars_indices[i] = index

hidden_word = replace_at_indices(word, stars_indices, "*")

# Sākam spēli, lūdzot lietotājam minēt burtus, līdz vārds tiks atminēts
while hidden_word != word:
    guess = input(f"Atminējiet vārdu: {hidden_word}\nIevadiet burtu: ")
    if guess in word:
        print("Atminējāt pareizi!")
        for i in range(len(word)):
            if word[i] == guess:
                stars_indices.remove(i)
        hidden_word = replace_at_indices(word, stars_indices, "*")
    else:
        print("Atminējāt nepareizi, mēģiniet vēlreiz.")

print(f"Apbrīnojami, jūs atminējāt vārdu '{word}'!")