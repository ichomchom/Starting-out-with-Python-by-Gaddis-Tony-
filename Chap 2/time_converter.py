total_second = float(input('Enter a number of seconds: '))

#get the hour
hour = total_second // 360

#get the minutes
minutes = (total_second // 60) % 60

#get the number of second
seconds = total_second % 60

print('Hour:' , hour)
print('Minutes:', minutes)
print('Seconds:', seconds)
