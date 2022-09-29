if __name__ == '__main__':
    my_string = 't1234h1234i1234saaaaiaaaasbbbbm1234yaaaapbbbbabbbbsaaaas1234'
    correct = my_string.replace('1234', '')
    correcta = correct.replace('aaaa', '')
    correctb = correcta.replace('bbbb', '')
    print(correctb)