weight = float(input('Enter the weight: '))
height =  float(input('Enter the height: '))

BMI = (weight * 703) / height**2

if BMI > 18.5 and BMI < 25:
    print('Your weight is gucci!')
    print(BMI)
elif BMI < 18.5:
    print('You are underweight!')
    print(BMI)
else:
    print('You are overweight')
    print(BMI)
