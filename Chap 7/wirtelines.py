def main():
    #Create list of strings
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']

    #Open file for writting
    outfile = open('cities.txt', 'w')

    #Write lsit to file
    outfile.writelines(cities)

    #Close file
    outfile.close()

main()    
