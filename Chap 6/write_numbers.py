#number convert to string before written to text file

def main():
    #Open file
    outfile = open('numbers.txt', 'w')

    #Get three numbers
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a number: '))
    num3 = int(input('Enter a number: '))

    #Write the number to file
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    #Close file
    outfile.close()
    print('Data written to numbers.txt')

main()
