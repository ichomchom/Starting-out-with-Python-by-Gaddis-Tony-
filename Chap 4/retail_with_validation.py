#Calculate retial prices

MARK_UP = 2.5
another = 'y'

#Process one or more items
while another == 'y' or another == 'Y':
    #Get the item's wholesale cost.
    wholesale = float(input("Enter the item's wholesale cost: "))

    #Validate the wholsale cost
    while wholesale < 0:
        print('ERROR: the cost cannot be negative.')
        wholesale = float(input('Enter the correct wholesale cost: '))

    #Calculate
    retail = wholesale * MARK_UP

    #Display
    print('Retail price: $', format(retail, ',.2f'), sep='')

    #Do this again
    another = input('Do you have another item? (Enter y for yes): ')
    
