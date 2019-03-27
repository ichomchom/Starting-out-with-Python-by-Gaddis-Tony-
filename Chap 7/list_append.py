def main():
    #Creat an empty list
    name_list = []

    #Var to control the loop
    again = 'y'

    #Add name to list
    while again == 'y':
        #Get name from the user
        name = input('Enter a name: ')

        #Append the name to the list
        name_list.append(name)

        #Add another one?
        print('Do you want to add another name?')
        again = input('y = yes, anything else = no: ')
        print()

    #Display the names that were entered
    print('Here are the names you enterd.')

    for name in name_list:
        print(name)

main()        
