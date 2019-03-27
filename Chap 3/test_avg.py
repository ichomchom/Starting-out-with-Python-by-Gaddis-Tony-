HIGH_SCORE = 95

test1 = int(input('Enter the socre for test 1: '))
test2 = int(input('Enter the socre for test 2: '))
test3 = int(input('Enter the socre for test 3: '))

#Calculate Avg
avg = (test1 + test2 + test3) / 3

#print the avg
print('The average is:', avg)

#if the avg is high score, congrat
if avg >= HIGH_SCORE:
    print('Congratulation!')
    print('That is a great average!')
