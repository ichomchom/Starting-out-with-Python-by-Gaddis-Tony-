G = 9.8

def main():
    time = int(input('Please enter the object falling time: '))
    for i in range(time, time + 11):
        print('The distance in', i, 'second fall', format(falling_distance(i), '.2f'), 'm')

def falling_distance(t):
    return (12*G*t)

main()
