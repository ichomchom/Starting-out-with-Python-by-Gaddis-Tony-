import person

def main():
    #Create empty list to hold the entry
    entry = []
    
    #Create loop to ask user input 3 persons information
    for count in range(0, 3):
        name = input('Enter name: ')
        address = input('Enter address: ')
        age = input('Enter age: ')
        phone = input('Enter phone number: ')

        #cearte entry
        entry.append(person.Person(name, address, age, phone))
        print()
        
    for info in entry:
        print(info)
        print()
main()
