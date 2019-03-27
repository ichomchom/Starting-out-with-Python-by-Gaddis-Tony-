#Class for patient
class Patient:
    def __init__(self, firstname, midname, lastname,
                 address, city, state, zipcode, phone, emer_name,
                 emer_phone):
        self.__firstname = firstname
        self.__midname = midname
        self.__lastname = lastname
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__phone = phone
        self.__emer_name = emer_name
        self.__emer_phone = emer_phone

    #Set methods
    def set_firstname(self, firstname):
        self.__firstname = firstname
        
    def set_midname(self, midname):
        self.__midname = midname
        
    def set_lastname(self, lastname):
        self.__lastname = lastname
        
    def set_address(self, address):
        self.__address = address
        
    def set_city(self, city):
        self.__city = city
        
    def set_state(self, state):
        self.__state = state
        
    def set_zipcode(self, zipcode):
        self.__zipcode = zipcode
        
    def set_phone(self, phone):
        self.__phone = phone
        
    def set_emer_name(self, emer_name):
        self.__emer_name = emer_name
        
    def set_emer_phone(self, emer_phone):
        self.__emer_phone = emer_phone

    #Get methods
    def get_firstname(self):
        return self.__firstname
        
    def get_midname(self):
        return self.__midname
        
    def get_lastname(self):
        return self.__lastname
        
    def get_address(self):
        return self.__address
        
    def get_city(self):
        return self.__city
        
    def get_state(self):
        return self.__state
        
    def get_zipcode(self):
        return self.__zipcode
        
    def get_phone(self):
        return self.__phone
        
    def get_emer_name(self):
        return self.__emer_name
        
    def get_emer_phone(self):
        return self.__emer_phone

    def __str__(self):
        return "Firt Name:" + self.__firstname +\
               "\nMiddle Name:" + self.__midname +\
               "\nLast Name:" + self.__lastname +\
               "\nAddress:" + self.__address +\
               "\nCity:" + self.__city +\
               "\nState:" + self.__state +\
               "\nZip Code:" + self.__zipcode +\
               "\nPhone:" + self.__phone +\
               "\nEmergency Contact Name:" + self.__emer_name +\
               "\nEmergency Contact Phone:" + self.__emer_phone

#Class for procedure
class Procedure:
    def __init__(self, name, date, pract, price):
        self.__name = name
        self.__date = date
        self.__pract = pract
        self.__price = price

    #Set methods
    def set_name(self, name):
        self.__name = name

    def set_date(self, date):
        self.__date = date

    def set_pract(self, pract):
        self.__pract = pract

    def set_price(self, price):
        self.__price = price
        
    #Get methods
    def get_name(self):
        return self.__name
    
    def get_date(self):
        return self.__date
    
    def get_pract(self):
        return self.__pract
    
    def get_price(self):
        return self.__price

    def __str__(self):
        return "Procedure name: " + self.__name +\
              "\nDate: " + self.__date +\
              "\nPractitioner: " + self.__pract +\
              "\nCharge: " + str(self.__price)
