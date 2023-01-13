a = input("Введите радиус круга: ")
otvet = float(a) ** 2
otvet2 = float(otvet) * 3.14
print("Площадь круга: " + (str(otvet2)))

if a1 <= a2 <= a3:
    print(a1, a2, a3)

    if a1 >= a2 >= a3:
        print(a3, a2, a1)

    elif a1 >= a2 <= a3:
        print(a2, a3, a1)

    elif a1 <= a2 >= a3:

