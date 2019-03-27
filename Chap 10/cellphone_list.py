import cellphone

def main():
    #Get a list of CellPhone objects
    phones = make_list()

    #Display data in the list
    print('Here is the data you entered:')
    display_list(phones)

def make_list():
    #Create an empty list
    phone_list = []

    #Add 5 CellPhone objects to list
    print('Enter data for 5 phones.')
    for count in range(1, 6):
        #Get phone data
        print('Phone number ' + str(count) + ':')
        man = input('Enter the manufacturer: ')
        mod = input('Enter the model number: ')
        retail = float(input('Enter the retail price: '))
        print()

        #Create new CellPhone object in memory and
        #assign it to phone variable
        phone = cellphone.CellPhone(man, mod, retail)

        #Add object to list
        phone_list.append(phone)

    return phone_list

#Display phone
def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()

main()
