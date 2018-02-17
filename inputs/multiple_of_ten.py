number = 0
try:
    number = raw_input('Input an integer, we\'ll tell if it\'s a multiple of 10: ')
    number = int(number)
    if number % 10 == 0:
        print(str(number) + ' is a multiple of 10')
    else:
        print(str(number) + ' is not a multiple of 10')
except ValueError:
    print('Oops! \'' + str(number) + '\' is not a integer!')