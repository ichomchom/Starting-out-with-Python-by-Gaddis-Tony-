import random

MIN = 1
MAX = 6

def main():
    #Var to control loop
    again = 'y'

    while again == 'y' or again == 'Y':
        print('Rolling the dice . . .')
        print()
        print('Their values are:')
        print(random.randint(MIN,MAX))
        print(random.randint(MIN,MAX))

        #Do again?
        again = input('Roll them again? (y = yes): ')

main()
