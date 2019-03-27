def main():
    string = input('Please enter your sentence: ')
    print(string[0], end='')
    for i in range(1, len(string)):
        if string[i].isupper():
            print(' ', end='')
            print(string[i].lower(), end='')
        else:
            print(string[i], end='')
            #list.append(string[i])
main()
