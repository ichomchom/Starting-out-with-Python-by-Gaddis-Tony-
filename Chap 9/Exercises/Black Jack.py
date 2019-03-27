import random

def main():
    #Create a deck of cards.
    deck = create_deck()

    #Deal the cards.
    deal_cards(deck)



def create_deck():
    #Create a dict with each card and its val
    #Stored as key-val pairs.
    deck = {'Ace of Spades' : 1, '2 of Spades' : 2, '3 of Spades' : 3,
            '4 of Spades' : 4, '5 of Spades' : 5, '6 of Spades' : 6,
            '7 of Spades' : 7, '8 of Spades' : 8, '9 of Spades' : 9,
            '10 of Spades' : 10, 'Jack of Spades' : 10,
            'Queen of Spades' : 10, 'King of Spades' : 10,
            
            'Ace of Hearts' : 1, '2 of Hearts' : 2, '3 of Hearts' : 3,
            '4 of Hearts' : 4, '5 of Hearts' : 5, '6 of Hearts' : 6,
            '7 of Hearts' : 7, '8 of Hearts' : 8, '9 of Hearts' : 9,
            '10 of Hearts' : 10, 'Jack of Hearts' : 10,
            'Queen of Hearts' : 10, 'King of Hearts' : 10,
            
            'Ace of Clubs' : 1, '2 of Clubs' : 2, '3 of Clubs' : 3,
            '4 of Clubs' : 4, '5 of Clubs' : 5, '6 of Clubs' : 6,
            '7 of Clubs' : 7, '8 of Clubs' : 8, '9 of Clubs' : 9,
            '10 of Clubs' : 10, 'Jack of Clubs' : 10,
            'Queen of Clubs' : 10, 'King of Clubs' : 10,
            
            'Ace of Diamonds' : 1, '2 of Diamonds' : 2, '3 of Diamonds' : 3,
            '4 of Diamonds' : 4, '5 of Diamonds' : 5, '6 of Diamonds' : 6,
            '7 of Diamonds' : 7, '8 of Diamonds' : 8, '9 of Diamonds' : 9,
            '10 of Diamonds' : 10, 'Jack of Diamonds' : 10,
            'Queen of Diamonds' : 10, 'King of Diamonds' : 10}

    return deck

def deal_cards(deck):
    #Initialize an accumulator for the hand value
    player1 = 0
    player2 = 0

    #Initialize max score
    max_score = 21

    
    while (player1 <= max_score) or (player2 <= max_score):


        
        #Get random value in the dictionary
        #Change dictionary into list vit key, val pairs
        card1, value1 = random.choice(list(deck.items()))
        print('player 1 draw: ', card1)

        #Add player score
        player1 += value1
        
        card2, value2 = random.choice(list(deck.items()))
        print('player 2 draw: ', card2)
        player2 += value2


        #If player get dealt an ace
        if (value1 == 1):

            #if the score + 11 less than 21 then Ace will count as 11
            #plus 10 because the ace at player += value already add 1
            #So only need 10
            if (player1 + 10) < 21:
                player1 += 10
  
            #If the score after +11 > 21
            #Then Ace will +1 only
            else:
                player1 = player1
                
        #If player get dealt an ace
        if (value2 == 1):

            #if the score + 11 less than 21 then Ace will count as 11
            #plus 10 because the ace at player += value already add 1
            #So only need 10
            if (player2 + 10) < 21:
                player2 += 10
  
            #If the score after +11 > 21
            #Then Ace will +1 only
            else:
                player2 = player2

        print('\n')
        #Check which player has score > 21 then stop the loop
        if (player1 > 21) or (player2 > 21):
            break


    #Display the value of the hand
    print('Value of player 1 hand:', player1)
    print('Value of player 2 hand:', player2)

    #Decide who win
    print('\n')
    if(player1 > 21) and (player2 < 21):
        print('Player 2 win.')
    elif(player2 > 21) and (player1 < 21):
        print('Player 1 win.')
    else:
        print('Tie.')

#Main
main()
