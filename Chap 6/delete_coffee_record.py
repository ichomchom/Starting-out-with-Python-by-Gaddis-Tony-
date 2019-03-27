import os #needed for remove and rename functions

def main():
    #Create bool var as flag
    found = False

    #Get the coffee to delete
    search = input('Which coffee do you want to delete? ')

    #Open the original coffee.txt
    coffee_file = open('coffee.txt', 'r')

    #Open the temp file
    temp_file = open('temp.txt', 'w')
    
    #Read the first record
    desc = coffee_file.readline()
    
    #Read the rest of file
    while desc != '':
        #Read the quantity field
        qty = float(coffee_file.readline())

        #Strip the \n
        desc = desc.rstrip('\n')

        #IF this is not the recrod del write to temp file
        if desc != search:
            temp_file.write(desc + '\n')
            temp_file.write(str(qty) + '\n')

        else:
            found = True

        #Read the next desc
        desc = coffee_file.readline()

    coffee_file.close()
    temp_file.close()

    #Del original file
    os.remove('coffee.txt')

    #Rename temp file
    os.rename('temp.txt', 'coffee.txt')

    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

main()        
    
