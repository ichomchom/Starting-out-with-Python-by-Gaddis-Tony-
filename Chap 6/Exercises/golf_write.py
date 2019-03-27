def main():
    #Create file
    file = open('golf.txt', 'w')
    file.write('Name\tRecord\n')

    #Ask how many players
    record = int(input('How many players: '))

    for i in range(1, record + 1):
        name = input('Enter player name: ')
        score = int(input('Player score: '))

        #write record to file
        file.write(name + '\t' + str(score) +'\n')

    #Close file
    file.close()

main()
