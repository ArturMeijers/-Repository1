def delatj_zvezdcki(text1):
    for symbol in text1:
        text1.replace(symbol, "*")
        return symbol
text1 = input()
print(delatj_zvezdcki(text1))



