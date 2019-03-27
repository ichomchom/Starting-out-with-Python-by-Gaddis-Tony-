import random

def main():
    amount = int(input('How many number you want to hold: '))
    file = open('random.txt', 'w')

    for i in range(amount):
        file.write(str(random.randint(1, 500)) + '\n')

    file.close()

main()
