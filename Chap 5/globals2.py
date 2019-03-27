number = 0

def main():
    global number
    number = int(input('Enter a number: '))
    show_num()

def show_num():
    print('The number you entered is', number)

main()
