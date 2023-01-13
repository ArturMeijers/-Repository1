Celsij1 = "C"
Celsij2 = "F"


a = input("Введите температуру: ")
b = input("По какой шкале ваша температура C/F? ")

a = int(a)

if b == Celsij1:
    otvetC = float(a) * float(9/5)
    otvet2 = 32 + float(otvetC)
    otvet3 = round(otvet2)
    print("Ваш ответ: " + (str(otvet3)) + " F")

    if a >= 0:
        print("Будет тепло")

    elif a <= 0:
        print("Будет холодно")



if b == Celsij2:
    otvetF = float(a) * float(9/5) + 32
    otvetF2 = round(otvetF)
    print("Ваш ответ: " + (str(otvetF2)))
