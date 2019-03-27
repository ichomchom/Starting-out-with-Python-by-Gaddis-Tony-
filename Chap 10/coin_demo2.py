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

#main func
def main():
    #Create an object Coin class
    my_coin = Coin()

    #Display the side of the coin that facing up
    print('This side is up:', my_coin.get_sideup())

    #Toss the coin
    print('I am tossing the coin ...')
    my_coin.toss()

    #Set attribute sideup to 'Heads'
    my_coin.sideup = 'Heads'

    #Display the side of the coin is facing up
    print('This side is up:', my_coin.get_sideup())
    
main()
