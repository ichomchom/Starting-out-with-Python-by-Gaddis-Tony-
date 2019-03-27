#Calculate retail prices

MARK_UP = 2.5 #Mark up percentage
another = 'y' # variable to controll the loop

#Process one or more item.
while another == 'y' or another == 'Y':
    #Get item's wholesale cost
    wholesale = float(input("Enter the item's wholesale cost: "))

    #Calculate the retail price
    retail = wholesale * MARK_UP

    #Display retail price
    print('Retail price: $', format(retail, ',.2f'), sep='')

    #Do again?
    another = input('Do you have another item? (Enter y for yes): ')
    
