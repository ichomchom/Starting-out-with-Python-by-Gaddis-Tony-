#this program cal 5 avg test score
#display each test with letter grade
def main():
    test1 = int(input('Please enter your 1st test: '))
    test2 = int(input('Please enter your 2nd test: '))
    test3 = int(input('Please enter your 3rd test: '))
    test4 = int(input('Please enter your 4th test: '))
    test5 = int(input('Please enter your 5th test: '))    
    print('Your average test score is: ', end='')
    print(calc_avg(test1, test2, test3, test4, test5))
    determine_grade(test1)
    determine_grade(test2)
    determine_grade(test3)
    determine_grade(test4)
    determine_grade(test5)
    
def calc_avg(test1, test2, test3, test4, test5):
    return (test1 + test2 + test3 + test4 + test5) / 5

def determine_grade(test):
    if test > 89:
        print('A')
    elif test > 79 and test < 90:
        print('B')
    elif test > 69 and test < 80:
        print('C')
    elif test > 59 and test < 70:
        print('D')
    else:
        print('F')
main()
