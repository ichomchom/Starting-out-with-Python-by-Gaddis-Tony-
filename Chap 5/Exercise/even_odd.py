import random


def main():
    EVEN = 0
    ODD = 0
    for i in range(100):
       if ((random.randint(0, 100) % 2) == 0):
            EVEN += 1
       else:
            ODD += 1

    print('Even: ', EVEN)
    print('Odd: ', ODD)

main()
