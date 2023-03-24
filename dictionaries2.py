# Izveidojam tukšu vārdnīcu, lai saglabātu datus
lietotaja_info = {}

# Uzjautājam lietotājam vārdu un saglabājam to vārdnīcā
lietotaja_vards = input("Ievadi savu vārdu: ")
lietotaja_info['vards'] = lietotaja_vards

# Uzjautājam lietotājam uzvārdu un saglabājam to vārdnīcā
lietotaja_uzvards = input("Ievadi savu uzvārdu: ")
lietotaja_info['uzvards'] = lietotaja_uzvards

# Izveidojam tukšu listu, lai saglabātu ēdienus
milietais_ediens = []
while True:
    # Uzjautājam lietotājam mīļāko ēdienu un saglabājam to listā
    ediena_nosaukums = input("Ievadi savu mīļāko ēdienu (ja vēlies pārtraukt, raksti 'stop'): ")
    if ediena_nosaukums == "stop":
        break
    else:
        milietais_ediens.append(ediena_nosaukums)

# Saglabājam ēdienu listu vārdnīcā
lietotaja_info['milakie_edieni'] = milietais_ediens

# Izvadam lietotāja informāciju uz ekrāna
print("Lietotāja informācija:")
print(f"Vārds: {lietotaja_info['vards']}")
print(f"Uzvārds: {lietotaja_info['uzvards']}")
print(f"Mīļākie ēdieni: {lietotaja_info['milakie_edieni']}")