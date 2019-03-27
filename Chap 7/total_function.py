def main():
    #Create a list
    numbers = [2, 4, 6, 8, 10]

    #Display total
    print('The total is', get_total(numbers))


def get_total(value_list):
    #Create var as accumulator
    total = 0

    #Cal total
    for num in value_list:
        total += num

    return total

main()
