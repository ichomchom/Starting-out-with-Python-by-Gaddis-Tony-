import random

def main():
    
    num = random.randint(0,100)
    ans = int(input('Please enter your guess: '))
    guess(num, ans)

def guess(num, ans):
    GUESS = 0
    while ans >= 0:
        if ans > num:
            print('Your guess is too high, guess again: ')
            GUESS += 1
            ans = int(input('Please enter your guess: '))
        elif ans < num:
            print('Your guess is too low, guess again: ')
            GUESS += 1
            ans = int(input('Please enter your guess: '))
        else:
            print('You are correct, the number is:', num)
            print('Your guess', GUESS, 'time.')
            break;

main()
