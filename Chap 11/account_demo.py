import accounts

def main():
    #Get account number, interest rate, and balance for saving account
    print('Enter the following data for a saving account.')
    acct_num = input('Account number: ')
    int_rate = float(input('Interest rate: '))
    balance = float(input('Balance: '))

    #Create SavingsAccount object
    savings = accounts.SavingsAccount(acct_num, int_rate, balance)

    #Get account number, interest rate, and balance
    #and maturity date for a CD
    print('Enter the following data for a CD.')
    acct_num = input('Account number: ')
    int_rate = float(input('Interest rate: '))
    balance = float(input('Balance: '))
    maturity = input('Maturity date: ')

    #Create SavingsAccount object
    cd = accounts.CD(acct_num, int_rate, balance, maturity)

    #Display data
    print('Here is the data you entered:')
    print()
    print('Savings Account')
    print('---------------')
    print('Account number:', savings.get_account_num())
    print('Interest rate:', savings.get_interest_rate())
    print('Balance: $', format(savings.get_balance(), ',.2f'), sep='')
    print()
    print('CD')
    print('---------------')
    print('Account number:', cd.get_account_num())
    print('Interest rate:', cd.get_interest_rate())
    print('Balance: $', format(cd.get_balance(), ',.2f'), sep='')
    print('Maturity date:', cd.get_maturity_date())

main()
