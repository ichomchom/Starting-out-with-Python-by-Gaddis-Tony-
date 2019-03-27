#This program count the number of time the letter T appear

def main():
    #Create var to hold the coount
    count = 0

    #Get string from the user
    my_string = input('Enter a sentence: ')

    #Count the Ts.
    for ch in my_string:
        if ch == 'T' or ch == 't':
            count += 1

    #Print result
    print('The letter T appears', count,'times.')

main()    
