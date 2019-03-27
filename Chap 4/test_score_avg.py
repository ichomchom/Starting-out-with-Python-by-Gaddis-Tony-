#Get num student
num_students = int(input('How many students do you have? '))

#Get number of test score per student
num_test_scores = int(input('How many test scores per student? '))

#Check test score
for student in range(num_students):
    #Initialize accumulator
    total = 0.0
    #Get student's test scores
    print('Student number', student + 1)
    print('---------------------')
    for test_num in range(num_test_scores):
        print('Test number', test_num + 1, end='')
        score = float(input(': '))
        #add the score to the accum
        total += score

    #Cal avg
    avg = total / num_test_scores

    #Display avg
    print('The average for student number', student + 1, 'is:', avg)
    print()
    
