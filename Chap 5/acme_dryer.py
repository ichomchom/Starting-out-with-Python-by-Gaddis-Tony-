#Disassembling Acme Dryer

def main():
    #Display start up message
    startup_message()
    input('Press Enter to see Step 1.')
    #Display step 1
    step1()
    input('Press Enter to see Step 2.')
    #Display step 2
    step2()
    input('Press Enter to see Step 3.')
    #Display step 3
    step3()
    input('Press Enter to see Step 4.')
    #Display step 4
    step4()

#Start up message
def startup_message():
    print('This program tells you how to disassemble an ACEM laundry dryer.')
    print('There are 4 steps in the process.')
    print()

#Display func for step 1
def step1():
    print('Step 1: Unplug the dryer and move it away from the wall.')
    print()
    
#func for step 2
def step2():
    print('Step 2: remove the six xcrews from the back of the dryer.')
    print()

#func for step 3
def step3():
    print('Step 3: Remove the back panel from the dryer.')
    print()

#func for step 4
def step4():
    print('Step 4: Pull the top of the dryer straight up.')

main()
