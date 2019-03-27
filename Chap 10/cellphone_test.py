import cellphone

def main():
    #Get phone data
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model number: ')
    retail = float(input('Enter the retail price: '))

    #Create instance of CellPhone class
    phone = cellphone.CellPhone(man, mod, retail)

    #Display the data
    print('Here is the data that you entered:')
    print('Manufacture:', phone.get_manufact())
    print('Model Number:', phone.get_model())
    print('Retail Price: $', format(phone.get_retail_price(), ',.2f'), sep='')

main()
