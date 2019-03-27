LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
    #Create empty birthday dictionary
    birthdays = {}

    #Initialize var for user's choice
    choice = 0

    while choice != QUIT:
        #Get the user's menu choice.
        choice = get_menu_choice()

        #Process the choice
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)

#Menu_choice func display the menu and validate choice from user
def get_menu_choice():
    print()
    print('Friends and Their Birthdays')
    print('---------------------------')
    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit the program')
    print()

    #Get the user's choice
    choice = int(input('Enter your choice: '))

    #Validate the choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice

#look up func
def look_up(birthdays):
    #Get name to look up
    name = input('Enter a name: ')

    #Look it up in dictionary
    print(birthdays.get(name, 'Not found.'))
    
#add function
def add(birthdays):
    #Get name and birthday
    name = input('Enter a name: ')
    bday = input('Enter a birthday: ')

    #If name does not exist, add it
    if name not in birthdays:
        birthdays[name] = bday
    else:
        print('That entry already exists.')

#chagne bday func
def change(birthdays):
    #Get name to look up
    name = input('Enter a name: ')

    if name in birthdays:
        #Get a new birthdays
        bday = input('Enter the new birthday: ')

        #Update birthday
        birthdays[name] = bday
    else:
        print('That name is not found.')

#Delete func
def delete(birthdays):
    #Get name to look up.
    name = input('Enter a name: ')

    #If name is found, delete
    if name in birthdays:
        del birthdays[name]
    else:
        print('That name is not found.')

main()        
