#Generate system login name
import login

def main():
    #Get user's first name, last name, and id
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    idnumber = input('Enter your student ID number: ')

    #Get login name
    print('Your system login name is:')
    print(login.get_login_name(first, last, idnumber))

#Call main
main()
