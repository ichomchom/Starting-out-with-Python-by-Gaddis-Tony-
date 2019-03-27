def main():

    file = open('numbers.txt', 'r')
    total = 0
    counter = 1
    
    for line in file:
        print(line, end='')
        total += int(line)
        counter += 1
    print('The average of all these number: ',total/counter)
    file.close()

main()    
