TUITION = 8000
PERCENATE = TUITION * .03

print('Year\tTuition')
for i in range (1, 6):
    new = TUITION + (PERCENATE * i)
    print(i,'\t',format(new, ',.0f'))
