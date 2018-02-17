no_of_guests = 0
try:
    no_of_guests = raw_input('How many people will be accompanying you for dinner: ')
    no_of_guests = int(no_of_guests)
    if no_of_guests > 8:
        print('You guys will have to wait for a table!')
    else:
        print('Your table is ready.')
except ValueError:
    print('Oops! \'' + str(no_of_guests) + '\' is invalid number of guests.')