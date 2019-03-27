#This program display property taxes

TAX_FACTOR = 0.0065

#Get the 1st lot num
print('Enter the property lot number')
print('or enter 0 to end.')
lot = int(input('Lost number: '))

#Loop enter 0 to end
while lot != 0:
    #Get property value
    value = float(input('Etner the property value: '))

    #Calculate the property's tax
    tax = value * TAX_FACTOR

    #Display the tax
    print('Property tax: $', format(tax, ',.2f'), sep='')

    #Get the next lot num
    print('Enter the next lot number or')
    print('enter 0 to end.')
    lot = int(input('Lot number: '))
    
