def main():
    #Create list of string
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']

    #Open file for write
    outfile = open('cities.txt', 'w')

    #Write lsit to file
    for item in cities:
        outfile.write(item + '\n')

    #Close file
    outfile.close()

main()    
