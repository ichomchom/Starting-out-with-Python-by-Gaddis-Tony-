totsec = int(input('Please enter second: '))

day = totsec // 86400
hour = totsec // 3600
minutes = (totsec // 60) % 60
sec = totsec % 60
if totsec < 3600:
    print('Minute:', totsec/60)
elif totsec < 86400:
    print('Hour:', totsec/3600)
else:
    print('Day:', day, 'Hour:', hour, 'Minutes:', minutes, 'Second:', sec )
