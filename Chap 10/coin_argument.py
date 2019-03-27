import coin

def main():
    #Create coin object
    my_coin = coin.Coin()

    #Display heads
    print(my_coin.get_sideup())

    #Pass the object to flip func
    flip(my_coin)

    #Display side up after flip
    print(my_coin.get_sideup())

#Flip func
def flip(coin_obj):
    coin_obj.toss()

main()
