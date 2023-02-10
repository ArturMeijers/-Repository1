def replace(string):
    result = ""
    for char in string:
        if char == " ":
            result += " "
        else:
            result += "*"
    return result
# def replace(string):
#     string.replace("*")

string = input("Enter text: ")
print(replace(string))


# input_string = input("Enter some text: ")
# print("".join(["*" for char in input_string]))
