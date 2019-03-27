#The Contact class holds contact information

class Contact:
    #The __init__ method initialize the attribues
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    #Set name method
    def set_name(self, name):
        self.__name = name

    #Set phone method
    def set_phone(self, phone):
        self.__phone = phone

    #Set email method
    def set_email(self, email):
        self.__email = email

    #Get name method
    def get_name(self):
        return self.__name

    #Get phone method
    def get_phone(self):
        return self.__phone

    #Get email method
    def get_email(self):
        return self.__email

    #The __str__ method return the object's state as string
    def __str__(self):
        return "Name : " + self.__name +\
               "\nPhone : " + self.__phone +\
               "\nEmail : " + self.__email
