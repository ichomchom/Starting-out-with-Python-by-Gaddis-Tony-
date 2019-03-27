sum = int(0)
total = int(0)
while sum >= 0:
    sum = int(input('Enter a positive number or negative number to end: '))
    if sum < 0:
        break
    total += sum
print(total)
