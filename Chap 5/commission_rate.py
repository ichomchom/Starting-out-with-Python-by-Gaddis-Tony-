def main():
    #Get amount of sale
    sales = get_sales()

    #Get amount of advanced pay
    advanced_pay = get_advanced_pay()

    #Determine the commission rate
    comm_rate = determine_comm_rate(sales)

    #Cal the pay
    pay = sales * comm_rate - advanced_pay

    #Display amont of pay
    print('The pay is $', format(pay, ',.2f'), sep ='')

    #Determine wether they pay is negative
    if pay < 0:
        print('The Salesperson must reimburse')
        print('the company.')
        
#get_sales func gets salesperson's montly sales and return value
def get_sales():
    #Get monthly sales
    monthly_sales = float(input('Enter the monthly sales: '))

    return monthly_sales

#get_advanced_pay func gets the amount of advanced pay given to salesperson
def get_advanced_pay():
    #Get advanced pay
    print('Enter the amount of advanced pay, or enter 0 if no advanced pay')
    print('was given.')
    advanced = float(input('Advanced pay: '))

    return advanced

#dertermine_comm_rate func accepts amount sale and return comm rate
def determine_comm_rate(sales):
    #Determine com rate
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.16
    else:
        rate = 0.18

    return rate

main() 
