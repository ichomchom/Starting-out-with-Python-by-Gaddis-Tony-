def main():
    #Open file for read
    infile = open('numberlist.txt', 'r')

    #Read contents of the file
    numbers = infile.readlines()

    #Close file
    infile.close()

    #Convert each elmt to int
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    print(numbers)

main()
