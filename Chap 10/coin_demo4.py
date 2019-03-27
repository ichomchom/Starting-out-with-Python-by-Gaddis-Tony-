import coin

def main():
    #Create object from Coin class
    my_coin = coin.Coin()

    #Display the side facing up
    print('This side is up:', my_coin.get_sideup())

    #Toss the coin
    print('I am going to toss the coin ten times:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

main()        
