def main():
    #Initialize an accumulator
    total = 0.0

    try:
        #open the sales_data.txt file
        infile = open('sales_data.txt', 'r')

        #Read the value form the file
        for line in infile:
            amount = float(line)
            total += tamount

        #close file
        infile.close()

        #Print the total
        print(format(total, ',.2f'))

    except IOError:
        print('An error occured trying to read the file.')

    except ValueError:
        print('Non-numeric data found in the file.')

    except:
        print('An error occured.')

main()
