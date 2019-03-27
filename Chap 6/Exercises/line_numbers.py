def main():
    file_name = input('Enter the file name: ')
    file = open(file_name, 'r')
    count = 1
    for line in file:
        print(str(count) + ',', end='')
        print(line)
        count += 1
    file.close()

main()    
