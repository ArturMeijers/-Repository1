a = input("Введите градусы: ")

b = input("C или F?: ")
if b == "C":
    a1 = float(a) * 9/5
    a2 = float(a1) + 32
    print("Градусы по фаренгейту: " + (str(round(a2))))
elif b == "F":
    a3 = float(a) - 32
    a4 = float(a3) * 5/9
    print("Градусы по цельсию: " + (str(round(a4))))








