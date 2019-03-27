def main():
    file = open('golf.txt', 'r')
    for line in file:
        print(line, end='')
    file.close()

main()    
