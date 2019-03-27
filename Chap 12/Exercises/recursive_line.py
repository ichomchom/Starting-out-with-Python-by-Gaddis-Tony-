def main():
    num = int(input('Please enter a number: '))

    line(num)

def line(n):
    if n > 0:
        line(n -1 )
        print('*' * n)

main()
