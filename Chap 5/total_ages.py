def main():
    #Get user's age
    first_age = int(input('Enter your age: '))

    #Get user's best friend's age
    second_age = int(input("Enter your best friend's age: "))

    #Get sum of both age
    total = sum(first_age, second_age)

    print('Together you are', total, 'years old.')

def sum(num1,num2):
    result = num1 + num2
    return result
main()
