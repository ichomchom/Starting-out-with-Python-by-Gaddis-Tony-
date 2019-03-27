def main():
    #Get number of days
    num_days = int(input('For how many days do you have sales? '))

    #Open new file for sales.txt
    sales_file = open('sales.txt', 'w')

    #Get the amount of sales for each day and write to file
    for count in range(1, num_days + 1):
        #Get sales for a day
        sales = float(input('Enter the sales for day #' + str(count) + ': '))

        #Write sales amount to file
        sales_file.write(str(sales) + '\n')

    #Close file
    sales_file.close()
    print('Data written to sales.txt.')

main()    
