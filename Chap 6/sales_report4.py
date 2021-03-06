def main():
    #Initialize an accumulator
    total = 0.0

    try:
        #Open sales_data.txt file
        infile = open('sales_data.txt', 'r')

        #Read value from file
        for line in infile:
            amount = float(line)
            total += amount

        #Close file
        infile.close()
    except Exception as err:
        print(err)
    else:
        #Print total
        print(format(total, ',.2f'))

main()
