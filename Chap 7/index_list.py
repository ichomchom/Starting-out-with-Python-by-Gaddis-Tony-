def main():
    #Create a list with some items
    food = ['Pizza', 'Burgers', 'Chips C']

    #Display list
    print('Here are the items in the food list:')
    print(food)

    #Get item to change
    item = input('Which item should I change? ')

    try:
        #Get the item's index in the list
        item_index = food.index(item)

        #Get the value to repace it with
        new_item = input('Enter the new value: ')

        #Replace the old item with new item
        food[item_index] = new_item

        #Display the list
        print('Here the revised list: ')
        print(food)
    except ValueError:
        print('That item was not found in the list.')

main()        
