def main():
    #Create a list of number
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #Get sum of items at indexes 2 trough 5
    my_sum = range_sum(numbers, 2, 5)

    #Display sum
    print('The sum of items 2 through 5 is', my_sum)

def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)

main()
