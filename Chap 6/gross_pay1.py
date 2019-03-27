def main():
    #Get the number of hours worked
    hours = int(input('How many hours did you work? '))

    #Get the hour pay rate
    pay_rate = float(input('Enter your hourly pay rate: '))

    #Calculate gross pay
    gross_pay = hours * pay_rate

    #Display gross pay
    print('Gross pay: $', format(gross_pay, '.2f'), sep='')

main()
