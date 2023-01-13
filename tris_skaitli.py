a1 = input("Введите первое число: ")
a2 = input("Введите второе число: ")
a3 = input("Введите третье число: ")

a1 = int(a1)
a2 = int(a2)
a3 = int(a3)

if a1 <= a2 <= a3:
    print(a1,a2,a3)

elif a1 <= a3 <= a2:
    print(a1,a3,a2)

elif a2 <= a1 <= a3:
    print(a2,a1,a3)

elif a3 <= a1 <= a2:
    print(a3, a1, a2)

elif a3 <= a2 <= a1:
    print(a3, a2, a1)

elif a2 <= a3 <= a1:
    print(a2, a3, a1)














