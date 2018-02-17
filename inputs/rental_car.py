cars = {'1':'Figo','2':'Swift','3':'Scorpio','4':'Mercedes'}
print('--------------------------------------------------------------')
print('Welcome to Zoomcar!')
print('--------------------------------------------------------------')
print('Which of following cars would you like to rent:')
print('  1: Figo')
print('  2: Swift')
print('  3: Scorpio')
print('  4: Mercedes')
selected_car = raw_input('> ')
car = cars.get(selected_car)
if car:
    print('Enjoy your ride with ' + car + '!\n  --Regards, Zoomcar\n')
else:
    print('Your input \'' + selected_car + '\' is invalid. Please specify the number of the car (Eg: 1,2,3, etc.)')