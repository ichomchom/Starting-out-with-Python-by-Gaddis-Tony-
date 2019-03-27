def main():
    #Open file
    coffee_file = open('coffee.txt', 'r')

    #Read the first discription field
    desc = coffee_file.readline()

    #Read the rest of file
    while desc != '':
        #Read quantity
        qty = float(coffee_file.readline())

        #Strip \n
        desc = desc.rstrip('\n')

        #Display
        print('Discription:', desc)
        print('Quantity:', qty)

        #Read the next description
        desc = coffee_file.readline()
        
    coffee_file.close()

main()
