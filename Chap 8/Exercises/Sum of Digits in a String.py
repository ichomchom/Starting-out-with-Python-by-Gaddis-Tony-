#Get sum of digit in the string
#Ex: 2514 => 2+5+1+4 = 12
def main():
    str = input('Enter digit string: ')
    sum = 0
    if str.isdigit():
        for chr in str:
            sum += int(chr)
    else:
        print('Not digit')

    print(sum)

main()    
