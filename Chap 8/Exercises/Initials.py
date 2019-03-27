def main():
    name = input('Please enter First Middle and Last name: ')

    name_list = name.split()

    print('Initials: ')
    for chr in name_list:
        print(chr[0] + '.')

main()
