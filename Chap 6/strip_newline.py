def main():
    #open philosophers.txt
    infile = open('philosophers.txt', 'r')

    #Read three lines from file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    #Strip the \n from each line
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    #Close file
    infile.close()

    print(line1)
    print(line2)
    print(line3)

main()
