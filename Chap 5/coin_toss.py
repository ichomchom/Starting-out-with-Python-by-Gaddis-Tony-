import random
HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print('Head')
        else:
            print('Tail')

main()            
