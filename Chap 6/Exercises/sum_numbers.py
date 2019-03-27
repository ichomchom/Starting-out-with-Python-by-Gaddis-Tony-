def main():

    file = open('numbers.txt', 'r')
    total = 0
    
    for line in file:
        print(line, end='')
        total += int(line)

    print('The total of all these number: ',total)
    file.close()

main()    
