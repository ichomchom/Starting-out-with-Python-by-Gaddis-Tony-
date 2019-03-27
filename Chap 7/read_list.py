def main():
    #Open file for read
    infile = open('cities.txt', 'r')

    #Read contesnt of file into a list
    cities = infile.readlines()

    #Close file
    infile.close()

    #Strip the \n from each element
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1

    print(cities)

main()    
