import random

def main():
    #Create list with 7 slots
    list = [0, 0, 0, 0, 0, 0, 0]

    for i in range(len(list)):
        list[i] = random.randint(0,9)

    print('The winning number is: ')
    print(list)

main()    
