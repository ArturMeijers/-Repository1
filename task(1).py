def replace(string):
    result = ""
    for char in string:
        if char == " ":
            result += " "
        else:
            result += "*"
    return result

string = input("Enter text: ")
print(replace(string))



