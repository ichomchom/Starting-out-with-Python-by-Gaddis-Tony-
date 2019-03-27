import random

num1 = random.randint(0,999)
num2 = random.randint(0,999)

def main():
    print(' ', num1)
    print('+', num2)
    ans = int(input('Enter your answer: '))
    check_answer(num1, num2, ans)

def check_answer(num1, num2, ans):
    if num1 + num2 == ans:
        print('Congrat!! Your answer is correct!!!')
    else:
        print('Wrong answer!! The answer is', num1 + num2)
main()
