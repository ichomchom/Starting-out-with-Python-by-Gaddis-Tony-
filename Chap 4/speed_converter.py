#Convert speed from 60 kph - 130 kph in 10 kph increments to mph

START_SPEED = 60
END_SPEED = 130
INCREMENT = 10
CONVERSION_FACTOR = 0.6214

print('KPH'.ljust(10,' ')+ 'MPH'.rjust(5, ' '))
print('-------------')

#Print speed
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(str(kph).ljust(9, ' '), str(format(mph, '.1f')).rjust(6, ' '))
