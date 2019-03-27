def main():
    #Create a bool var to use as a flag
    found = False

    #Get search value
    search = input('Enter a escription to search for: ')

    #Open coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    #Read the first record's description field
    desc = coffee_file.readline()

    #Get the rest of the file
    while desc != '':
        #Read the quantity field
        qty = float(coffee_file.readline())

        #Strip the \n from desc
        desc = desc.rstrip('\n')

        #Determine whether the recrod matches the search value
        if desc == search:
            #Display record
            print('Description:', desc)
            print('Quantity:', qty)
            print()
            #Set the found flag to True
            found = True

        #Read next desc
        desc = coffee_file.readline()

    coffee_file.close()

    #If the search value not found
    if not found:
        print('That item was not found in the file.')

main()        
