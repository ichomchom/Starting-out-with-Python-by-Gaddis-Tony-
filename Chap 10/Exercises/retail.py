class RetailItem:
    def __init__(self, descrp, unit, price):
        self.__descrp = descrp
        self.__unit = unit
        self.__price = price


    #Set methods
    def set_descrp(self, descrp):
        self.__descrp = descrp

    def set_unit(self, unit):
        self.__unit = unit

    def set_price(self, price):
        self.__price = price

    #Get methods

    def get_descrp(self):
        return self.__descrp

    def get_unit(self):
        return self.__unit

    def get_price(self):
        return self.__price

    def __str__(self):
        return "\t" + self.__descrp +\
               "\t\t\t" + self.__unit +\
               "\t\t" + self.__price

class CashRegister:
    #list hold items
    item_list = []

    #list hold purchase items
    purchase_list = []

    #list hold total price
    total_list = []

    #Create the RetailItem object
    def __init__(self):
        RetailItem.item
        
