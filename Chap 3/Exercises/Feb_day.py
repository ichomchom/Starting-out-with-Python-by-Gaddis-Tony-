year = int(input('Please enter year: '))

if year % 100 == 0:
    if year % 400 == 0:
        print('Feb has 29 days')
elif year % 4 == 0:
    print('Feb has 29 days')
else:
    print('Regular Feb')
