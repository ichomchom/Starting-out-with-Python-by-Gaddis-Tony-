def main():
    string = input('Enter your string: ')
    string_list = string.split()
    for i in string_list:
        print(i[1:] + i[0] + 'AY', end=' ')

main()
