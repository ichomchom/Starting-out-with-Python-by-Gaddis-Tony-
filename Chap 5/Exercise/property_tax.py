PERCENTAGE = 0.6
TAX = 0.72
value = float(input('Enter the value of the property: '))
assessment = value * PERCENTAGE
property_tax = (assessment/100) * TAX

print('Your assessmen value: $', format(assessment, ',.2f'), sep='')
print('Your property tax: $', format(property_tax, ',.2f'), sep='')
