BASE_HOUR = 40 #base hours per week
OT_MULTIPLIER = 1.5 #overtime multiply

#Get hours worked and hourly pay
hours = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))

if hours > BASE_HOUR:
    #cal gross with OT
    #Get num of overtime worked
    overtime = hours - BASE_HOUR

    #calculate overtime pay
    overtime_pay = overtime * pay_rate * OT_MULTIPLIER
    
    #calculate gross
    gross = BASE_HOUR * pay_rate + overtime_pay
else:
    #calculate gross with no OT
    gross = BASE_HOUR * pay_rate

#Display Gross pay
print('The gross pay is $', format(gross ,',.2f'), sep = '')
