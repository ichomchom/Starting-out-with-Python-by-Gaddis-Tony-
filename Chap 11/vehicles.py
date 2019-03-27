#Autombile class holds general data about the automobile

class Automobile:
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price


    #Set methods

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    #Get methods

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

#The Car class representes a car. It is a subclass of the Automobile class

class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        #Call superclass's __init__ method and pass required arguements
        Automobile.__init__(self, make, model, mileage, price)

        #Initialize the __doors attribue
        self.__doors = doors

    #Set method
    def set_doors(self, doors):
        self.__doors = doors

    #Get method
    def get_doors(self):
        return self.__doors

#The truck class representes pickup truck
class Truck(Automobile):
    def __init__(self, make, model, mileage, price, drive_type):
        Automobile.__init__(self, make, model, mileage, price)

        #Initialize drive_type
        self.__drive_type = drive_type

    #Set method
    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    #Get method
    def get_drive_type(self):
        return self.__drive_type

class SUV(Automobile):
    def __init__(self, make, model, mileage, price, pass_cap):
        Automobile.__init__(self, make, model, mileage, price)

        #Initialize pass cap
        self.__pass_cap = pass_cap

    #Set method
    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    #Get method
    def get_pass_cap(self):
        return self.__pass_cap
    
