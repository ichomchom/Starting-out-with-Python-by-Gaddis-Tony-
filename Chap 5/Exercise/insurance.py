PERCENTAGE = 0.08

amount = float(input('Please enter the cost of the building: '))
insurance = amount * PERCENTAGE
print('The minimum amount of insurance for your property', format(insurance, ',.2f'))
