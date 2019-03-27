def main():
    #Open file
    infile = open('philosophers.txt', 'r')

    #Read 3 lines from file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    #close file
    infile.close()

    #print data
    print(line1)
    print(line2)
    print(line3)

main()
