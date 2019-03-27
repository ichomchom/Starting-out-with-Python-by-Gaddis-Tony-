import login

def main():
    #Get pass from user
    password = input('Enter your password: ')

    #Validate pass
    while not login.valid_password(password):
        print('That password is not valid.')
        password = input('Enter your password: ')

    print('That is a valid password.')

main()
