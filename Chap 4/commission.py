#This program cal sales com

#Create control loop
keep_going = 'y'

while keep_going == 'y':
    #Get salesperson's sales and com rate
    sales = float(input('Enter the amount of sales: '))
    com_rate = float(input('Enter the commission rate: '))

    #cal culate
    commission = sales * com_rate

    #Display
    print('The commission is $', format(commission, ',.2f'), sep = '')

    #Condition check
    keep_going = input('Do you want to calculate another commision ' + 
                       '(Enter y for yes):')
