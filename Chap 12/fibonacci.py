def main():
    print('The first 10 number in the Fibonacci serires are:')

    for number in range(1, 11):
        print(fib(number))

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

main()
