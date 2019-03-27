
def main():
    for i in range(101):
        is_prime(i)

def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    print(num)

main()
