import employee
import pickle

#Menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#Filename
FILENAME = 'employee.dat'

def main():
    #Load the exist data into employee dictionary
    employ_dict = load_employee()

    #initialize the choice
    choice = 0

    while choice != QUIT:
        #Get user's choice
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(employ_dict)
        elif choice == ADD:
            add(employ_dict)
        elif choice == CHANGE:
            change(employ_dict)
        elif choice == DELETE:
            delete(employ_dict)

    #save information
    save_info(employ_dict)

def load_employee():
    try:
        #open the file
        infile = open(FILENAME, 'rb')

        #unpickle the data
        employ_dict = pickle.load(infile)

        #close the file
        infile.close()
    except IOError:
        #If the file not found, create an empty dictionary
        employ_dict = {}

    return employ_dict
    
def get_menu_choice():
    print()
    print('Menu')
    print('----------------')
    print('1. Look up employee')
    print('2. Add new employee')
    print('3. Make a change for employee')
    print('4. Delete an employee')
    print('5. Quit the program')
    print()

    choice = int(input('Enter your choice: '))

    while choice < LOOK_UP and choice > QUIT:
        choice = int(input('Please enter a valid choice: '))

    return choice

def look_up(employ_dict):
    
    print('Look up Employee!!!')
    #Get user's input for id number
    id_num = input('Please enter ID number: ')

    #Print infomation base on id number if not in dictionary
    #default message will show up
    print(employ_dict.get(id_num, 'That ID is not found.'))

def add(employ_dict):
          
    print('Add new Employee!!!')
    name = input('Enter name: ')
    id_num = input('Enter ID number: ')
    dept = input('Enter Department: ')
    title = input('Enter Title: ')

    #create entry
    entry = employee.Employee(name, id_num, dept, title)

    #Check if ID already in dictionary if not add the entry
    if id_num not in employ_dict:
        employ_dict[id_num] = entry
        print('New employee added.')
    else:
        print('Employee already exist.')

def change(employ_dict):
    print('Make a change!!!')
    id_num = input('Please enter ID number: ')

    if id_num in employ_dict:

        #Get new inputs
        name = input('Enter name: ')
        dept = input('Enter department: ')
        title = input('Enter title: ')

        #Create entry to add to dictionary
        entry = employee.Employee(name, id_num, dept, title)

        #Update employee
        employ_dict[id_num] = entry
        print('Information updated.')
    else:
        print('That ID is not found.')

def delete(employ_dict):
    print('Delete employee!!!')
    id_num = input('Enter ID number: ')

    if id_num in employ_dict:
        del employ_dict[id_num]
        print('Employee deleted.')
    else:
        print('ID number is not found.')

def save_info(employ_dict):
    #Create file to write
    outfile = open(FILENAME, 'wb')
    pickle.dump(employ_dict, outfile)
    outfile.close()

main()

