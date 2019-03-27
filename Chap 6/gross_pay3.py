def main():
    try:
        #Get the number of hours worked
        hours = int(input('How many hours did you work? '))

        #Get the hoursly pay rate
        pay_rate = float(input('Enter your hourly pay rate: '))

        #Cal gross pay
        gross_pay = hours * pay_rate

        #Display the gross pay
        print('Gross pay: $', format(gross_pay, '.2f'), sep='')
    except ValueError as err:
        print(err)

main()        
