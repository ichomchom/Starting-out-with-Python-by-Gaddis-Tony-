#This program assists a technician in the process checking substance's temp

#Declare max temp
MAX_TEMP = 102.5

#Get the substance's temp
temp = float(input("Enter the substance's Celsius temperature: "))

#Instruct user to adjust the thermostat
while temp > MAX_TEMP:
    print('The temperature is too high.')
    print('turn the thermostat down and wait')
    print('5 minutes. Then take the temperature')
    print('again and enter it.')
    temp = float(input('Enter the new Celsius temperature: '))

#Remind user to check again in 15 mins
print('The temperature is acceptable.')
print('Check it agian in 15 minutes.')
