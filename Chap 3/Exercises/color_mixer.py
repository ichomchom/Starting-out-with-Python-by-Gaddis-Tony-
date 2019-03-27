color1 = input('Please enter color 1: ')
if color1 != 'red' and color1 != 'yellow' and color1 != 'blue':
    print('Please enter red, yellow, or blue')
    
color2 = input('Please enter color 2: ')
if color2 != 'red' and color2 != 'yellow' and color2 != 'blue':
    print('Please enter red, yellow, or blue')
    
if color1 == 'red' and color2 == 'blue':
    print('Your mixed is purple.')
elif color1 == 'red' and color2 == 'yellow':
    print('Your mixed is orange.')
elif color1 == 'blue' and color2 == 'yellow':
    print('Your mixed is green.')
else:
    print('Please enter red, yellow, or blue')
