import os #Need to import this to remove and rename file

def main():
    #Create bool var to use as flag
    found = False

    #Get the search value and the new quantity
    search = input('Enter a description to search for: ')
    new_qty = int(input('Enter the new quantity: '))

    #Open the original coffee.txt
    coffee_file = open('coffee.txt', 'r')

    #Open the temp file
    temp_file = open('temp.txt', 'w')

    #Read the first desc
    desc = coffee_file.readline()

    while desc != '':
        #Read the quantity
        qty = float(coffee_file.readline())

        #Strip the \n from desc
        desc = desc.rstrip('\n')

        #Write the record to temp file, or new record if
        #it is the one to be modified
        if desc == search:
            #Write the modified reacord to temp file
            temp_file.write(desc + '\n')
            temp_file.write(str(new_qty) + '\n')

            #Set flag to true
            found = True
        else:
            #Write the original record to temp
            temp_file.write(desc + '\n')
            temp_file.write(str(qty) + '\n')

        #Read the next desc
        desc = coffee_file.readline()

    #Close files
    coffee_file.close()
    temp_file.close()

    #Delete the original coffee.txt
    os.remove('coffee.txt')

    #Rename the temp file
    os.rename('temp.txt', 'coffee.txt')

    #If search not found in file
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

main()
