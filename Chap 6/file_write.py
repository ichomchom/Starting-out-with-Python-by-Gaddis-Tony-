def main():
    #Open file named philosophers.txt
    outfile = open('philosophers.txt', 'w')

    #Write names to the files
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    #Close file
    outfile.close()

main()
