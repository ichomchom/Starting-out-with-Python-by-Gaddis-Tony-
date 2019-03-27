import retail

def main():

    #Create empty list to hold entry
    entry = []

    item = int(input('How many items you want to enter: '))

    for count in range(0, item):
        descrp = input('Enter item description: ')
        unit = input('Enter unit in inventory: ')
        price = input('Enter price of the items: ')

        entry.append(retail.RetailItem(descrp, unit, price))

    print('\tDescription \tUnit in inventory \tPrice')
    for count in range(0, len(entry)):
        print('Item #' + str(count +1)+ str(entry[count]))

main()
