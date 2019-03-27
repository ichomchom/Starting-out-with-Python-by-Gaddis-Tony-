def main():
    #Open file for reading
    infile = open('numbers.txt', 'r')

    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    #Close file
    infile.close()

    #Add 3 nums
    total = num1 + num2 + num3

    #Print total
    print('The numbers are:', num1, num2, num3)
    print('The total:', total)

main()
