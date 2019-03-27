def main()
    #Initialize the square
    square = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    enter_square(square)
    check_square(square)

#Input the square into 2D list
def enter_square(list):
    print('Please enter your magic square:')
    for i in range(3):
        for j in range(3):
            list[i][j] = int(input())
    return list
                
#Check if the square is Lo Shu Square
def check_square(list):
    if LTR(list) == TLBR(list) == BLTR(list) == TTB(list):
        print('This is Lo Shu Magic Square')
    else:
        print('This is not a Lo Shu Magic Square')

#Calculate sum from Left to Right
def LTR(list):
    for i in list:
        return sum(i)

#Calculate sum from Top Left to Bottom Right diagnose
def TLBR(list):
    sum = 0
    for i in range(3):
        sum +=(list[i][i])
    return sum

#Calculate Bottom Left to Top Right diagnose
def BLTR(list):
    sum = 0
    j = 2
    for i in range(3):
        sum +=(list[i][j])
        j -= 1
    return sum

#Calculate from Top to Bottom
def TTB(list):
    sum = 0
    for i in range(3):
        for j in range(3):
            sum +=(list[j][i])
        return( sum)
        sum = 0
        
main()
