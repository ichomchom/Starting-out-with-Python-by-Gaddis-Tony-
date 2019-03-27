def main():
    #Create list
    food = ['Pizza', 'Burgers', 'Chips']

    #Display list
    print('Here the list: ')
    print(food)

    #Get the item to change
    item = input('Which item should I remove? ')

    try:
        #Remove item
        food.remove(item)

        #Display list
        print('Here the revised list:')
        print(food)

    except ValueError:
        print('That item was not found in the list.')

main()
