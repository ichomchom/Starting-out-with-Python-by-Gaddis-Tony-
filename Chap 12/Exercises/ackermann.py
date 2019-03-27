def main():
    m = int(input('Please enter number m: '))
    n = int(input('Please enter number n: '))

    print(ackermann(m, n))

def ackermann(m, n):
    if m == 0:
        return (n + 1)
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n-1))

main()
