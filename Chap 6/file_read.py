def main():
    #Open file named philosophers.txt.
    infile = open('philosophers.txt', 'r')

    #Read file content
    file_contents = infile.read()

    #Close file
    infile.close()

    #print data that read into memory
    print(file_contents)

main()
