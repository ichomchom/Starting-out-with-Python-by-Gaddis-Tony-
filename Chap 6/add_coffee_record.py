def main():
    #Create var control loop
    another = 'y'

    #Open the coffee.txt in append mode
    coffee_file = open('coffee.txt', 'a')

    #Add records to file
    while another == 'y' or another == 'Y':
        #Get coffee record data
        print('Enter the following coffee data:')
        desc = input('Description: ')
        qty = int(input('Quantity (in pounds): '))

        #Append data to file
        coffee_file.write(desc + '\n')
        coffee_file.write(str(qty) + '\n')

        #Determine whether user want to add more
        print('Do you want to add another record?')
        another = input('Y = yes, anithing else = no: ')

    #close file
    coffee_file.close()
    print('Data appended to coffee.txt.')

main()
