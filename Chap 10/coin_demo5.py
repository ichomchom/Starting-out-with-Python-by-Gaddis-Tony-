import coin

def main():
    #Create 3 objects from Coin class
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    #Display the side facing up
    print('I have three coins with these side up:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

    #Toss the coin
    print('I am going to toss all three coins ...')
    print()
    coin1.toss()
    coin1.toss()
    coin1.toss()

    #Display the side facing up
    print('Now here are the sides that are up')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()
main()        
