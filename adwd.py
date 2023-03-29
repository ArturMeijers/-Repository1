lietotaja_info = {}

lietotaja_vards = input("Ievadi savu vārdu: ")
lietotaja_info['vards'] = lietotaja_vards

lietotaja_uzvards = input("Ievadi savu uzvārdu: ")
lietotaja_info['uzvards'] = lietotaja_uzvards

milietais_ediens = ""
while True:
    ediena_nosaukums = input("Ievadi savu mīļāko ēdienu (ja vēlies pārtraukt, raksti 'stop'): ")
    if ediena_nosaukums == "stop":
        break
    else:
        milietais_ediens += ediena_nosaukums + ", "

milietais_ediens = milietais_ediens.rstrip(", ")
lietotaja_info['milakie_edieni'] = milietais_ediens

print("Lietotāja informācija:")
print("Vārds: " + lietotaja_info['vards'])
print("Uzvārds: " + lietotaja_info['uzvards'])
print("Mīļākie ēdieni: " + lietotaja_info['milakie_edieni'])