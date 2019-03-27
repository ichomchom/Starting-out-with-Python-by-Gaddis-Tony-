NUM_EMPLOYEES = 6

def main():
    #Createa  list to hold employee hours
    hours = [0] * NUM_EMPLOYEES

    #Get employee's hours worked
    for index in range(NUM_EMPLOYEES):
        print('Enter the hours work by employee ', index + 1, ': ', sep='', end='')
        hours[index] = float(input())

    #Get the hourly pay rate
    pay_rate = float(input('Enter the hourly pay rate: '))

    #Display each employee's gross pay
    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print('Gross pay for employee ', index + 1, ': $',
              format(gross_pay, ',.2f'), sep='')

main()
