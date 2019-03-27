def main():
    phone = input('Please enter phone number in XXX-XXX-XXXX format: ')
    phone_list = phone.split('-')
    string1 = 'ABC'
    string2 = 'DEF'
    string3 = 'GHI'
    string4 = 'JKL'
    string5 = 'MNO'
    string6 = 'PQRS'
    string7 = 'TUV'
    string8 = 'WXYZ'
    print(phone_list[0],end = '')
    for i in range (1 , len(phone_list)):
        print('-', end='')
        for char in phone_list[i]:
            if char in string1:
                print('2', end='')
            if char in string2:
                print('3', end='')
            if char in string3:
                print('4', end='')
            if char in string4:
                print('5', end='')
            if char in string5:
                print('6', end='')
            if char in string6:
                print('7', end='')
            if char in string7:
                print('8', end='')
            if char in string8:
                print('9', end='')
        
        
#A, B, and C = 2
#D, E, and F = 3
#G, H, and I = 4
#J, K, and L = 5
#M, N, and O = 6
#P, Q, R, and S = 7
#T, U, and V = 8
#W, X, Y, and Z = 9

main()
