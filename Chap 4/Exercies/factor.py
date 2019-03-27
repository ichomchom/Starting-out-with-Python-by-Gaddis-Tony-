num = int(input('Enter a positive number: '))
total = int(1)
while num < 0:
    num = int(input('Enter a positive number: '))
for i in range (1, num + 1):
    total = i * total
print(total)

    
