#Get the desired future value
future_value = float(input('Enter the desired future value: '))

#Get the annual interest rate
rate = float(input('Enter the annual interest rate: '))

#Get the number of year
years = int(input('Enter the number of years: '))

#Calculation
present_value = future_value / (1.0 + rate) ** years

#Display
print('You will need to deposit this amount:', present_value)
