chet_numbers = []
nechet_numbers = []
numbers = []
print("Вводите числа. Чтобы закончить операцию введите 'viss'")
while True:
    user_input = input("Вводите числа: ")
    if user_input == "viss":
        break
    number = int(user_input)
    numbers.append(user_input)
    if number % 2 == 0:
        chet_numbers.append(number)
    else:
        nechet_numbers.append(number)

# while user_input.isalpha:
#     break
#     if user_input.isalpha == False:
print("Все числа:", numbers)
print("Четные числа:", chet_numbers)
print("Нечетные числа:", nechet_numbers)





