def main():
    file = open('random.txt', 'r')
    counter = 0
    print('The random numbers are: ')
    for i in file:
        print(i, end='')
        counter += 1
        
    print('Total numbers:', counter)        
    file.close()

main()    
