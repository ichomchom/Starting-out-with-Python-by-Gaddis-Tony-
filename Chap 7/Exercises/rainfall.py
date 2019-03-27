def main():
    rainfall = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total = 0
 
    
    for i in range(len(rainfall)):
        print('Please enter the amount of rain for', i + 1, 'month: ', end='')
        rainfall[i] = int(input())
        total += rainfall[i]

    print('The total rainfall this year:', total)
    print('The average rainfall this year:', total/len(rainfall)+1)
    print('The month with highest rainfall:', max(rainfall))
    print('The month with lowest rainfall:', min(rainfall))

main()    
    
