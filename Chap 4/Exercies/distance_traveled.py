speed = int(input('Enter the speed of the vehicle? '))
hour = int(input('How many horus has it traveled? '))

print('Hour\tDistance Traveled')
for i in range(1,hour + 1):
    distance = speed * i
    print(i,'\t',distance)
