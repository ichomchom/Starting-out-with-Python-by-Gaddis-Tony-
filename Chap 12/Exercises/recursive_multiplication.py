def main():
    num1 = int(input('Please enter x: '))
    num2 = int(input('Please enter y: '))

    print(multi(num1, num2))

    
def multi(x, y):
    if x == 1:
        return y
    else:
        return y + multi(x - 1, y)
main()
