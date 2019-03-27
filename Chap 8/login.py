#get_login name func accept first name last name, id and
#return system login name

def get_login_name(first, last, idnumber):
    #Get first three letters of firstname
    set1 = first[0:3]

    #Get first three letters of lastname
    set2 = last[0:3]

    #Get the last three numbers of ID
    set3 = idnumber[-3:]

    login_name = set1 + set2 + set3

    return login_name

#valid_password func accepts password as an argument
#return either true of false to indicate whether password is valid
#Valid pass must be at least 7 chars in length, at least one uppercase
#one lowercase and one digit.

def valid_password(password):
    #Set the Boolean variables to false.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    #Begin validation
    if len(password) >= 7:
        correct_length = True

        #Test each char
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

    #Determine all requirements are met.
    #If they are, set is_valid to true
    if correct_length and has_uppercase and has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False

    #Return is_valid
    return is_valid
