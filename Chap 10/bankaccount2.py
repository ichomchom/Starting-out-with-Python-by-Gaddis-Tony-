class BankAccount:
    #__init__ method accepts an argument for the account's balance.
    def __init__(self, bal):
        self.__balance = bal

    #The deposit method
    def deposit(self, amount):
        self.__balance += amount

    #The withdraw method
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficent funds')

    #get_balance method return the account balance
    def get_balance(self):
        return self.__balance

    #The __str__ method returns a string
    #indicating the object's state
    def __str__(self):
        return 'The balance is $' + format(self.__balance, ',.2f')
    
