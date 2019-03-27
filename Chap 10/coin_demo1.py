import random

class Coin:
    #The _ _init_ _ method initializes the side up data
    #attribute with 'Heads'.

    def __init__(self):
        self.sideup = 'Heads'

    #The toss method generates a random number in the rang of
    #0 throuhg 1. If the number is 0, then sideup is set to 'Heads'.
    #Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Head'
        else:
            self.sideup = 'Tails'

    #The get_sideup method returns the value referenced by sideup.

    def get_sideup(self):
        return self.sideup

#Main fuc
def main():
    #Create an object from Coin class
    my_coin = Coin()

    #Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())

    #Toss the coin.
    print('I am tossing the coin ...')
    my_coin.toss()

    #Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())

#Call main func
main()
