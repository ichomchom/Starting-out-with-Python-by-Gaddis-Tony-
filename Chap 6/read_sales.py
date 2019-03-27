def main():
    #Open sales.txt file for reading
    sales_file = open('sales.txt', 'r')

    #Read first line from the file
    #don't conver to number yet
    #Need it to test for empty string
    line = sales_file.readline()

    #As long as empty string is not returned from readline, continue
    while line != '':
        #Convert line to float
        amount = float(line)

        #Format and display the amount
        print(format(amount, '.2f'))

        #Read the next line
        line = sales_file.readline()

    sales_file.close()

main()
