import pickle

LOOK_UP = 1
ADD = 2
UPDATE = 3
DELETE = 4
QUIT = 5

def main():
    #initialize user's choice
    choice = 0
      
    emails = {}

    #Open file for reading
    infile = open('NameEmail.dat', 'rb')

    #load file into emails dictionary
    emails = pickle.load(infile)

    infile.close()
    
    while choice != QUIT:
        #get user's choice
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(emails)
        elif choice == ADD:
            add(emails)
        elif choice == UPDATE:
            update(emails)
        elif choice == DELETE:
            delete(emails)
        else:
            dump_data(emails)
        

def get_menu_choice():        
    print()
    print('List of name and emails')
    print('-----------------------')
    print('1. Look up email')
    print('2. Add email')
    print('3. Update email')
    print('4. Delete email')
    print('5. Quit')

    #Get user's choice
    choice = int(input('Enter your choice: '))

    #Check if the choice is valid
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice

#Look up
def look_up(emails):
    name = input('Enter name for look up: ')
    print(name, 'email is: ')

    #Get email from name if not in dictionary show default msg
    print(emails.get(name, 'Not found.'))
    
def add(emails):
    name = input('Please enter name: ')
    email = input('Please enter email: ')

    #Check if name is in dictionary
    if name not in emails:
        emails[name] = email
    else:
        print('That entry already exist!')
    
def update(emails):
    name = input('Enter a name to change email: ')

    #Check if name is in dictionary
    if name in emails:
        email = input('Enter new email: ')

        #Update email
        emails[name] = email
        
    else:
        print('That name is not found.')
        
    
def delete(emails):
    name = input('Enter a name to delete: ')

    if name in emails:
        del emails[name]
    else:
        print('That name is not found.')

def dump_data(emails):
    #Open file for writing
    outfile = open('NameEmail.dat', 'wb')

    #Dump dictionary into NameEmail.dat
    pickle.dump(emails, outfile)

    #close file
    outfile.close()
    
main()
