import contact
import pickle

#Global constanst for Menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#Global constanst for filename
FILENAME = 'contacts.dat'

def main():
    #Load existing contact dictionary and assisn it to mycontacts
    mycontacts = load_contacts()

    #initialize choice
    choice = 0

    while choice != QUIT:
        #Get the user's menu chocie
        choice = get_menu_choice()

        #Process the choice
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    #Save mycontacts dictionary to file
    save_contacts(mycontacts)

def load_contacts():
    try:
        #Open contacts.dat file
        infile = open(FILENAME, 'rb')

        #unpickle dictionary
        contact_dct = pickle.load(infile)

        #Close file
        infile.close()
    except IOError:
        #could not open the file, so create an empty dict
        contact_dct = {}
    return contact_dct

def get_menu_choice():
    print()
    print('Menu')
    print('-------------------')
    print('1. Look up a contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact')
    print('5. Quit the program')
    print()

    #Get the user's choice
    choice = int(input('Enter your choice: '))

    while choice < LOOK_UP and choice >QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice

def look_up(mycontacts):
    name = input('Enter a name: ')

    print(mycontacts.get(name, 'That name is not found.'))

def add(mycontacts):
    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')

    #Create Contact object name entry
    entry = contact.Contact(name, phone, email)

    #If the name does not exist in dictionary
    #add it
    if name not in mycontacts:
        mycontacts[name] = entry
        print('The entry has been added.')
    else:
        print('The name already exists.')

def change(mycontacts):
    name = input('Enter a name: ')

    if name in mycontacts:
        #Get new data
        phone = input('Enter new phone number: ')
        email = input('Enter new email address: ')

        #Create entry
        entry = contact.Contact(name, phone, email)

        #update entry
        mycontacts[name] = entry
        print('Information updated.')
    else:
        print('That name is not found.')

def delete(mycontacts):
    name = input('Enter a name: ')

    if name in mycontacts:
        del mycontacts[name]
        print('Entry deleted.')
    else:
        print('That name is not found.')

def save_contacts(mycontacts):
    outfile = open(FILENAME, 'wb')
    pickle.dump(mycontacts, outfile)
    outfile.close()
    
main()



