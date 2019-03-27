def main():
    #Create list of num
    numbers = [1, 2, 3, 4, 5, 6, 7]

    #Open file for write
    outfile = open('numberlist.txt', 'w')

    #Write list to file
    for item in numbers:
        outfile.write(str(item) + '\n')

    outfile.close()

main()    
