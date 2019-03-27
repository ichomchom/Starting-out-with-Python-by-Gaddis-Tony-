def main():
    #Get number from user.
    number = int(input('Enter a nonnegative interger: '))

    #Get factorial of number
    fact = factorial(number)

    print('The factorial of', number, 'is', fact)

#Calculate the factorial of its argument
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

main()
