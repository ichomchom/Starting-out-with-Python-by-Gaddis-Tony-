import pet

def main():
    
    name = input('Enter pet name: ')
    pet_type = input('Enter pet type: ')
    age = input('Enter pet age: ')

    #Create instance
    petobj = pet.Pet(name, pet_type, age)

    #Dislay
    print('Here the information you enter')
    print('Pet name: ', petobj.get_name())
    print('Pet type: ', petobj.get_type())
    print('Pet age: ', petobj.get_age())

main()    
    
