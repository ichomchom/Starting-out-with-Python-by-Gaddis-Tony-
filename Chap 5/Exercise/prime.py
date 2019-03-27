
def main():
    num = int(input('Enter a number: '))
    print(is_prime(num))

def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True
main()
