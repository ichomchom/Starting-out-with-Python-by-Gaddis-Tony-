#demonstrates passing two strings as keyword arguments to a func

def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reserved is')
    reserve_name(last = last_name, first = first_name)

def reserve_name(first, last):
    print(last, first)

main()
