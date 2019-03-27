import random

class Coin:
    #The __init__ method initializes the side up is "Heads'

    def __init__(self):
        self.__sideup = 'Heads'

    #Toss method
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    #return the value by referenced
    def get_sideup(self):
        return self.__sideup

def main():
    #create object coin class
    my_coin = Coin()

    #Display side up
    print('This side is up:', my_coin.get_sideup())

    #Toss coin
    print('I am going to toss the coin ten times: ')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

main()
