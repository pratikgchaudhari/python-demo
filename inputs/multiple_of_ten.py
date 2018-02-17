number = int(raw_input('Input a number, we\'ll tell if it\'s a multiple of 10: '))
if number % 10 == 0:
    print(str(number) + ' is a multiple of 10')
else:
    print(str(number) + ' is not a multiple of 10')