class SavingsAccount:

    def __init__(self, account_num, int_rate, bal):
        self.__account_num = account_num
        self.__interest_rate = int_rate
        self.__balance = bal

    #Set methods
    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_interest_rate(self, int_rate):
        self.__interest_rate = int_rate

    def set_balance(self, bal):
        self.balance = bal

    #Get methods
    def get_account_num(self):
        return self.__account_num

    def get_interest_rate(self):
        return self.__interest_rate

    def get_balance(self):
        return self.__balance

#CD account represents a certificate of deposit (CD) account.
#It is a subclass of SavingsAccount class
class CD(SavingsAccount):
    def __init__(self, account_num, int_rate, bal, mat_date):
        SavingsAccount.__init__(self, account_num, int_rate, bal)

        #Initialize the __maturity_date attribute
        self.__maturity_date = mat_date

    def set_maturity_date(self, mat_date):
        self.__maturity_date = mat_date

    def get_maturity_date(self):
        return self.__maturity_date
    
