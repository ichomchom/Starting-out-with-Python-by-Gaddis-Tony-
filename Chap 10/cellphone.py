#CellPhone class holds data bout a cell phone
class CellPhone:
    #The __init__ method initializes the attributes

    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    #Set the manufact method to accepts an argument for
    #the phone's manufacturer
    def set_manufac(self, manufact):
        self.__manufact = manufact

    #Set the model method to accept argument for the
    #phone's model number
    def set_model(self, model):
        self.__model = model

    #Set retial price
    def set_retail_price(self, price):
        self._retail_price = price

    #Return methods
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
    
