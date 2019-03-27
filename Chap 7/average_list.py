def main():
    #Create a list
    scores = [2.5, 7.3, 6.5, 4.0, 5.2]

    #Create var as accumulator
    total = 0.0

    #Cal the total
    for value in scores:
        total += value

    #Cal the avg
    avg = total / len(scores)

    print('The average of the elements is', avg)

main()    
