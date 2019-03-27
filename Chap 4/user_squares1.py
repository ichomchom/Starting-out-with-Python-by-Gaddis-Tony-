#Use loop to display table of number and their square

print('This program displyas a list of numbers')
print('(starting at 1) and their squares.')
end = int(input('How high should I go?'))

#Print table headings.
print()
print('Number\tSquare')
print('---------------')

#Print numbers and their square
for number in range(1, end + 1):
    square = number**2
    print(number, '\t', square)
