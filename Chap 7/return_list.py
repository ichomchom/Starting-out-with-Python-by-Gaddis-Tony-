def main():
    #Get list with value
    numbers = get_values()

    #Display value in list
    print('The numbers in the list are:')
    print(numbers)

def get_values():
    #create empty list
    values = []

    #Create a var control loop
    again = 'y'

    #Get values from user
    while again == 'y' :
        #Get number and add to list
        num = int(input('Enter a number: '))
        values.append(num)

        #Continue?
        print('Do you want to add another number?')
        again = input('y = yes, anything else = no: ')
        print()

    #return list
    return values

main()
