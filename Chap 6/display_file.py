def main():
    #Get the name of file
    filename = input('Enter a filename: ')

    #Open the file
    infile = open(filename, 'r')

    #Read the file's contents
    contents = infile.read()

    #Display file's contents
    print(contents)

    infile.close()

main()
