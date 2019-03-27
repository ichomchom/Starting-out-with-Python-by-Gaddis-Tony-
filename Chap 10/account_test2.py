import bankaccount2

def main():
    #GEt the starting balance
    start_bal = float(input('Enter your starting balance: '))

    #Create a BankAccount object
    savings = bankaccount2.BankAccount(start_bal)

    #Deposit user's paycheck
    pay = float(input('How much were you paid this week? '))
    print('I will deposit that into your account.')
    savings.deposit(pay)

    #Display the balance
    print(savings)

    #Get the amount to withdraw
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your accont.')
    savings.withdraw(cash)

    #Display the balance
    print(savings)

main()
