
b = [1, 3, 5, 6, 8, 7, 9]
#b = int(input("Напишите число: "))
for b in range(1, 7):
    if b <= 1:
        print(b, "Ваше число не четное")
    else:
        if b % 2 == 0:
            print(b, "Ваше число четное" )
        else:
            print(b, "Ваше число не четное")



