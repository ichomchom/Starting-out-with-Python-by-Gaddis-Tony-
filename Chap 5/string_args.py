#Pass string to func
def main():
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    print('Your name reserved is')
    reserve(first, last)

def reserve(first, last):
    print(last, first)

main()
