#use loop to display a table show 1 - 10 and their square

#print table headings.
print('Number\tSqare')
print('--------------')

#print numbers 1 through 10 and their square
for number in range(1, 11):
    square = number**2
    print(number, '\t', square)
