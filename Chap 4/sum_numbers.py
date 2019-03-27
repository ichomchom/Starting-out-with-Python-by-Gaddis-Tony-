#Calculate the sum of series
#Max num
MAX = 5

#initialize accumulator variable
total = 0.0

print('This program calculates the sum of')
print(MAX, 'numbers you will enter.')

#Get the number and accumulate them
for counter in range(MAX):
    number = int(input('Enter a number: '))
    total = total + number

#Display total
print('The total is', total)
