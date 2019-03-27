import math

def main():
    #Get the length of the trigangle's two sides
    a = float(input('Enter the length of side A: '))
    b = float(input('Enter the length of side B: '))

    c = math.hypot(a, b)

    print('The length of the hypotense is', c)

main()
