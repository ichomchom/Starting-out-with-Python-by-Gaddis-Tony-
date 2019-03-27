def main():
    num = int(input('Enter a number: '))

    recurs(num)

def recurs(num):
    if num > 0:
        recurs(num - 1)
        print(num)

main()
