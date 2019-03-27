def main():

    num = int(input('Please enter a number greater than 1: '))

    print(check_prime(num))


#Check prime number
#check from 2 to the number - 1
#EX for number 9: 9 % 3 == 0 so return False
#EX for number 11: 11 % 2,3,4,5,6,7,8,9,10 != 0 so return True
def check_prime(num):
    prime_list = []

    #Check from 2 to the number enter
    for i in range(2, num):
        isPrime = True

        #check from the range 2 to i
        for j in range(2, i):
            if (i % j  == 0):
                isPrime = False

        #If isPrime is true add it to the list
        if isPrime:
            prime_list.append(i)

    #return the list
    return prime_list
main()
