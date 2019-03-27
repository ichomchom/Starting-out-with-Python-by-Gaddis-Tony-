import random

class Coin:
    #Initialize the sideup data with Heads
    def __init__(self):
        self.__sideup = 'Heads'

    #Toss method
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    #get_sideup method return val

    def get_sideup(self):
        return self.__sideup
