def main():
    #display intro
    intro()
    #Get number of cups
    cups_needed = int(input('Enter the number of cups: '))
    #conver cups to ounces
    cups_to_ounces(cups_needed)

#intro func
def intro():
    print('This program converts measurements')
    print('in cups to ffluid ounces. For your')
    print('reference the formula is:')
    print('1 cup = 8 fluid ounces')
    print()

#cups_to_ounces func
def cups_to_ounces(cups):
    ounces = cups * 8
    print('That converts to', ounces, 'ounces.')

#Call main
main()
